# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from autorest.codegen.models.schema_response import SchemaResponse
from typing import Any, Dict, List, TypeVar, Optional, Callable

from .base_builder import BaseBuilder, get_converted_parameters
from .request_builder_parameter import RequestBuilderParameter
from .request_builder_parameter_list import RequestBuilderParameterList
from .schema_request import SchemaRequest
from .imports import FileImport, ImportType, TypingSection


T = TypeVar('T')
OrderedSet = Dict[T, None]

def _non_binary_schema_media_types(media_types: List[str]) -> OrderedSet[str]:
    response_media_types: OrderedSet[str] = {}

    json_media_types = [media_type for media_type in media_types if "json" in media_type]
    xml_media_types = [media_type for media_type in media_types if "xml" in media_type]

    if not sorted(json_media_types + xml_media_types) == sorted(media_types):
        raise ValueError("The non-binary responses with schemas of {self.name} have incorrect json or xml mime types")
    if json_media_types:
        if "application/json" in json_media_types:
            response_media_types["application/json"] = None
        else:
            response_media_types[json_media_types[0]] = None
    if xml_media_types:
        if "application/xml" in xml_media_types:
            response_media_types["application/xml"] = None
        else:
            response_media_types[xml_media_types[0]] = None
    return response_media_types

class RequestBuilder(BaseBuilder):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        url: str,
        method: str,
        multipart: bool,
        schema_requests: List[SchemaRequest],
        parameters: RequestBuilderParameterList,
        description: str,
        summary: str,
        responses: Optional[List[SchemaResponse]] = None,
    ):
        super().__init__(
            yaml_data=yaml_data,
            name=name,
            description=description,
            parameters=parameters,
            responses=responses,
            summary=summary,
        )
        self.url = url
        self.method = method
        self.multipart = multipart
        self.schema_requests = schema_requests

    @property
    def is_stream(self) -> bool:
        """Is the request we're preparing a stream, like an upload."""
        return any(request.is_stream_request for request in self.schema_requests)

    @property
    def has_body_param_with_object_schema(self) -> bool:
        try:
            parameters = self.parameters.body
            return any([p for p in parameters if p.has_object_schema])
        except ValueError:
            return False

    @property
    def operation_group_name(self) -> str:
        return self.yaml_data["language"]["python"]["operationGroupName"]

    def imports(self, code_model) -> FileImport:
        file_import = FileImport()
        for parameter in self.parameters:
            file_import.merge(parameter.imports())

        core_import = (code_model.namespace if code_model.options["vendor"] else "azure") + ".core.rest"
        file_import.add_from_import(
            core_import,
            "HttpRequest",
            ImportType.AZURECORE,
        )
        if self.parameters.path:
            file_import.add_from_import(
                "azure.core.pipeline.transport._base", "_format_url_section", ImportType.AZURECORE
            )
        file_import.add_from_import(
            "typing", "Any", ImportType.STDLIB, typing_section=TypingSection.CONDITIONAL
        )
        return file_import

    @staticmethod
    def get_parameter_converter() -> Callable:
        return RequestBuilderParameter.from_yaml

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], *, code_model) -> "RequestBuilder":

        names = [
            "build",
            yaml_data["language"]["python"]["name"],
            "request"
        ]
        name = "_".join([n for n in names if n])

        first_request = yaml_data["requests"][0]

        parameters, multiple_media_type_parameters = (
            get_converted_parameters(yaml_data, cls.get_parameter_converter())
        )

        request_builder_class = cls(
            yaml_data=yaml_data,
            name=name,
            url=first_request["protocol"]["http"]["path"],
            method=first_request["protocol"]["http"]["method"].upper(),
            multipart=first_request["protocol"]["http"].get("multipart", False),
            schema_requests=[SchemaRequest.from_yaml(yaml) for yaml in yaml_data["requests"]],
            parameters=RequestBuilderParameterList(parameters + multiple_media_type_parameters),
            description=yaml_data["language"]["python"]["description"],
            responses=[SchemaResponse.from_yaml(yaml) for yaml in yaml_data.get("responses", [])],
            summary=yaml_data["language"]["python"].get("summary"),
        )
        code_model.request_builder_ids[id(yaml_data)] = request_builder_class
        return request_builder_class

    @property
    def has_example_template(self) -> bool:
        if self.parameters.has_body:
            body_kwargs = set(self.parameters.body_kwarg_names.keys())
            return bool(body_kwargs.intersection({"json", "files"}))
        return bool(self.get_json_response_template_to_status_codes())