# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
from copy import deepcopy
from collections.abc import MutableSequence
import logging
from typing import cast, List, Callable, Optional, TypeVar, Dict, Set

from .parameter import Parameter, ParameterLocation
from .object_schema import ObjectSchema
from .constant_schema import ConstantSchema
from .base_schema import BaseSchema
from .primitive_schemas import IOSchema, ByteArraySchema

T = TypeVar('T')
OrderedSet = Dict[T, None]

_LOGGER = logging.getLogger(__name__)


class ParameterList(MutableSequence):
    def __init__(
        self, parameters: Optional[List[Parameter]] = None
    ) -> None:
        self.parameters = parameters or []
        self.json_body: Optional[BaseSchema] = None
        self._multipart_parameters: Optional[Set[Parameter]] = set()

    # MutableSequence

    def __getitem__(self, index):
        if isinstance(index, str):
            raise TypeError(f"{index} is invalid type")
        return self.parameters[index]

    def __len__(self) -> int:
        return len(self.parameters)

    def __setitem__(self, index, parameter):
        self.parameters[index] = parameter

    def __delitem__(self, index):
        del self.parameters[index]

    def insert(self, index: int, value: Parameter) -> None:
        self.parameters.insert(index, value)

    # Parameter helpers

    def has_any_location(self, location: ParameterLocation) -> bool:
        return bool([parameter for parameter in self.parameters if parameter.location == location])

    def get_from_predicate(self, predicate: Callable[[Parameter], bool]) -> List[Parameter]:
        return [parameter for parameter in self.parameters if predicate(parameter)]

    def get_from_location(self, location: ParameterLocation) -> List[Parameter]:
        return self.get_from_predicate(lambda parameter: parameter.location == location)

    @property
    def has_body(self) -> bool:
        return self.has_any_location(ParameterLocation.Body)

    @property
    def body(self) -> List[Parameter]:
        if not self.has_body:
            raise ValueError(f"Can't get body parameter")
        # Should we check if there is two body? Modeler role right?
        body_params = self.get_from_location(ParameterLocation.Body)
        if not self.json_body:
            try:
                json_param = next(p for p in body_params if not isinstance(p.schema, IOSchema))
                self.json_body = deepcopy(json_param.schema)
            except StopIteration:
                pass
        return body_params

    @staticmethod
    def _wanted_path_parameter(parameter: Parameter):
        # TODO add 'and parameter.location == "Method"' as requirement to this check once
        # I can use send_request on operations.
        # Don't want to duplicate code from send_request.
        return parameter.location == ParameterLocation.Uri and parameter.rest_api_name != "$host"

    @property
    def implementation(self) -> str:
        return "Method"

    @property
    def path(self) -> List[Parameter]:
        return [
            parameter
            for parameter in self.parameters
            if self._wanted_path_parameter(parameter)
        ]

    @property
    def query(self) -> List[Parameter]:
        return self.get_from_location(ParameterLocation.Query)

    @property
    def headers(self) -> List[Parameter]:
        headers = self.get_from_location(ParameterLocation.Header)
        if not headers:
            return headers
        return list({
            header.serialized_name: header
            for header in headers
        }.values())

    @property
    def grouped(self) -> List[Parameter]:
        return self.get_from_predicate(lambda parameter: cast(bool, parameter.grouped_by))

    @property
    def groupers(self) -> List[Parameter]:
        groupers: List[Parameter] = []
        for parameter in self.parameters:
            if any([
                p for p in self.grouped
                if p.grouped_by and id(p.grouped_by.yaml_data) == id(parameter.yaml_data)
            ]):
                groupers.append(parameter)
        return groupers

    @property
    def constant(self) -> List[Parameter]:
        """Return the constants of this parameter list.

        This excludes the constant from flatening on purpose, since technically they are not
        constant from this set of parameters, they are constants on the models and hence they do
        not have impact on any generation at this level
        """
        return self.get_from_predicate(
            lambda parameter: parameter.constant
        )

    @property
    def constant_bodies(self) -> List[Parameter]:
        constants = self.constant
        if not constants:
            return []
        return [c for c in constants if c.location == ParameterLocation.Body]

    @property
    def has_multipart(self) -> bool:
        return any(self.get_from_predicate(lambda parameter: parameter.is_multipart))

    @property
    def has_partial_body(self) -> bool:
        return any(self.get_from_predicate(lambda parameter: parameter.is_partial_body))

    @property
    def content_types(self) -> List[str]:
        content_type_params = self.get_from_predicate(
            lambda parameter: parameter.serialized_name == "content_type"
        )
        content_types: OrderedSet[str] = {}
        for param in content_type_params:
            if isinstance(param.schema, ConstantSchema):
                content_types[param.schema.value] = None
            else:
                # enums
                content_types.update({v.value: None for v in param.schema.values})

        return list(content_types.keys())

    @property
    def default_content_type(self) -> str:
        json_content_types = [c for c in self.content_types if "json" in c]
        if json_content_types:
            if "application/json" in json_content_types:
                return "application/json"
            return json_content_types[0]

        xml_content_types = [c for c in self.content_types if "xml" in c]
        if xml_content_types:
            if "application/xml" in xml_content_types:
                return "application/xml"
            return xml_content_types[0]
        return self.content_types[0]

    @property
    def method(self) -> List[Parameter]:
        """The list of parameter used in method signature.
        """
        signature_parameters_no_default_value = []
        signature_parameters_default_value = []

        # Client level should not be on Method, etc.
        parameters_of_this_implementation = self.get_from_predicate(
            lambda parameter: parameter.implementation == self.implementation
        )
        for parameter in parameters_of_this_implementation:
            if parameter.in_method_signature:
                if not parameter.default_value and parameter.required:
                    signature_parameters_no_default_value.append(parameter)
                else:
                    signature_parameters_default_value.append(parameter)

        signature_parameters = signature_parameters_no_default_value + signature_parameters_default_value
        return signature_parameters

    def method_signature(self, async_mode: bool) -> List[str]:
        positional = self.method_signature_positional(async_mode)
        kwargs = self.method_signature_kwargs(async_mode)
        return positional + kwargs

    def method_signature_positional(self, async_mode: bool) -> List[str]:
        return [parameter.method_signature(async_mode) for parameter in self.method if not parameter.is_kwarg]

    @property
    def kwargs(self) -> List[Parameter]:
        return [p for p in self.method if p.is_kwarg]

    @property
    def kwargs_to_pop(self) -> List[Parameter]:
        return [m for m in self.method if m.is_kwarg]

    def method_signature_kwargs(self, async_mode: bool) -> List[str]:
        leftover_kwargs_typing = ["**kwargs: Any"] if async_mode else ["**kwargs  # type: Any"]
        if not async_mode:
            return leftover_kwargs_typing
        kwargs_signature = [parameter.method_signature(async_mode) for parameter in self.kwargs]
        asterisk = ["*,"] if kwargs_signature else []
        return asterisk + kwargs_signature + leftover_kwargs_typing

    @property
    def is_flattened(self) -> bool:
        return cast(bool, self.get_from_predicate(lambda parameter: parameter.flattened))

    def build_flattened_object(self) -> str:
        if not self.is_flattened:
            raise ValueError("This method can't be called if the operation doesn't need parameter flattening")

        parameters = self.get_from_predicate(
            lambda parameter: parameter.in_method_code
        )
        parameter_string = ", ".join(
            [f"{param.target_property_name}={param.serialized_name}"
            for param in parameters if param.target_property_name
            ]
        )
        object_schema = cast(ObjectSchema, self.body[0].schema)
        return f"{self.body[0].serialized_name} = _models.{object_schema.name}({parameter_string})"

    def get_files_template_representation(self) -> str:
        template = {
            param.serialized_name: param.schema.get_files_template_representation(
                optional=not param.required,
                description=param.description,
            )
            for param in self._multipart_parameters
        }
        return json.dumps(template, sort_keys=True, indent=4)

    def get_json_template_representation(self) -> str:
        return json.dumps(self.json_body.get_json_template_representation(), sort_keys=True, indent=4)

class GlobalParameterList(ParameterList):

    @property
    def implementation(self) -> str:
        return "Client"

    @staticmethod
    def _wanted_path_parameter(parameter: Parameter) -> bool:
        return (
            parameter.location == ParameterLocation.Uri and
            parameter.implementation == "Client" and
            parameter.rest_api_name != "$host"
        )
