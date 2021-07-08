# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from functools import partial
from autorest.codegen.models.schema_request import SchemaRequest
from itertools import groupby
from autorest.codegen.models.operation import NoModelOperation
from autorest.codegen.models.parameter import Parameter
import json
from collections import defaultdict
from abc import abstractmethod, ABC
from autorest.codegen.models.request_builder import RequestBuilder
from autorest.codegen.models.base_builder import BaseBuilder
from typing import Any, Callable, List, TypeVar, Dict, Union, Optional
from ..models import (
    Operation,
    CodeModel,
    PagingOperation,
    LROOperation,
    LROPagingOperation,
    BaseBuilder,
    ObjectSchema,
    DictionarySchema,
    ListSchema,
)
from . import utils

T = TypeVar('T')
OrderedSet = Dict[T, None]

def _serialize_json_dict(template_representation: str, indent: int = 4) -> Any:
    # only for template use, since it wraps everything in strings
    return json.dumps(template_representation, sort_keys=True, indent=indent)

def _serialize_files_dict(multipart_parameters: List[Parameter]) -> str:
    # only for template use
    template = {
        param.serialized_name: param.schema.get_files_template_representation(
            optional=not param.required,
            description=param.description,
        )
        for param in multipart_parameters
    }
    return json.dumps(template, sort_keys=True, indent=4)

def _serialize_parameters_dict(parameters: List[Parameter], dict_name: str, value_callable: Callable) -> List[str]:
    retval = [f"{dict_name} = {{"]
    for parameter in parameters:
        retval.append(f"    \"{parameter.rest_api_name}\": {value_callable(parameter)},")
    retval.append("}")
    return retval

class BuilderSerializerProtocol(ABC):

    @property
    @abstractmethod
    def _is_in_class(self) -> bool:
        ...

    @property
    @abstractmethod
    def _function_definition(self) -> str:
        """The def keyword for the function, i.e. 'def' or 'async def'"""
        ...

    @property
    @abstractmethod
    def _want_inline_type_hints(self) -> bool:
        """Whether you want inline type hints. If false, your type hints will be commented'"""
        ...

    @abstractmethod
    def _method_signature(self, builder: BaseBuilder) -> str:
        """Signature of the builder. Does not include return type annotation"""
        ...

    @abstractmethod
    def _response_type_annotation(self, builder: BaseBuilder, modify_if_head_as_boolean: bool = True) -> str:
        """The mypy type annotation for the response"""
        ...

    @abstractmethod
    def _response_type_annotation_wrapper(self, builder: BaseBuilder) -> List[str]:
        """Any wrappers that you want to go around the response type annotation"""
        ...

    @staticmethod
    @abstractmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, _response_type_annotation: str) -> str:
        """Template for how to combine the method signature + the response type annotation together. Called by
        method_signature_and_response_type_annotation"""
        ...

    @abstractmethod
    def method_signature_and_response_type_annotation(self, builder: BaseBuilder) -> str:
        """Combines the method signature + the response type annotation together"""
        ...

    @abstractmethod
    def description_and_summary(self, builder: BaseBuilder) -> List[str]:
        """Description + summary from the swagger. Will be formatted into the overall operation description"""
        ...

    @abstractmethod
    def response_docstring(self, builder: BaseBuilder) -> List[str]:
        """Response portion of the docstring"""
        ...

    @abstractmethod
    def _content_type_docstring(self, builder: BaseBuilder) -> str:
        """Docstring for content type kwarg"""

    @abstractmethod
    def want_example_template(self, builder: BaseBuilder) -> bool:
        ...

    @abstractmethod
    def get_example_template(self, builder: BaseBuilder) -> List[str]:
        ...

    @abstractmethod
    def _get_json_example_template(self, builder: BaseBuilder) -> List[str]:
        ...

    @abstractmethod
    def _has_json_example_template(self, builder: BaseBuilder) -> bool:
        ...

    @abstractmethod
    def _has_files_example_template(self, builder: BaseBuilder) -> bool:
        ...

    @abstractmethod
    def _json_example_param_name(self, builder: BaseBuilder) -> str:
        ...

    @abstractmethod
    def _get_files_example_template(self, builder: BaseBuilder) -> List[str]:
        ...

    @abstractmethod
    def _get_json_response_template(self, builder: BaseBuilder) -> List[str]:
        ...

    @abstractmethod
    def _get_json_response_template_to_status_codes(self, builder: BaseBuilder) -> Dict[str, List[Union[str, int]]]:
        ...

    @abstractmethod
    def _serialize_path_format_parameters(self, builder: BaseBuilder) -> List[str]:
        ...

    @abstractmethod
    def _get_kwargs_to_pop(self, builder: BaseBuilder) -> List[Parameter]:
        ...

    @abstractmethod
    def pop_kwargs_from_signature(self, builder: BaseBuilder) -> List[str]:
        ...

class BuilderBaseSerializer(BuilderSerializerProtocol):
    def __init__(self, code_model: CodeModel) -> None:
        self.code_model = code_model

    def _method_signature(self, builder: BaseBuilder) -> str:
        return utils.serialize_method(
            function_def=self._function_definition,
            method_name=builder.name,
            is_in_class=self._is_in_class,
            method_param_signatures=builder.parameters.method_signature(self._want_inline_type_hints)
        )

    def _response_type_annotation_wrapper(self, builder: BaseBuilder) -> List[str]:
        return []

    def method_signature_and_response_type_annotation(self, builder: BaseBuilder) -> str:
        method_signature = self._method_signature(builder)
        response_type_annotation = self._response_type_annotation(builder)
        for wrapper in self._response_type_annotation_wrapper(builder)[::-1]:
            response_type_annotation = f"{wrapper}[{response_type_annotation}]"
        return self._method_signature_and_response_type_annotation_template(method_signature, response_type_annotation)

    def description_and_summary(self, builder: BaseBuilder) -> List[str]:
        description_list: List[str] = []
        description_list.append(f'{ builder.summary.strip() if builder.summary else builder.description.strip() }')
        if builder.summary and builder.description:
            description_list.append("")
            description_list.append(builder.description.strip())
        description_list.append("")
        return description_list

    def param_description(self, builder: BaseBuilder) -> List[str]:
        description_list: List[str] = []
        for parameter in [m for m in builder.parameters.method if m.is_documented]:
            description_list.extend(f":{parameter.description_keyword} { parameter.serialized_name }: { parameter.description }".replace('\n', '\n ').split("\n"))
            description_list.append(f":{parameter.docstring_type_keyword} { parameter.serialized_name }: { parameter.docstring_type }")
        try:
            request_builder: RequestBuilder = builder.request_builder
        except AttributeError:
            request_builder: RequestBuilder = builder

        if len(request_builder.schema_requests) > 1:
            description_list.append(self._content_type_docstring(builder))
        return description_list

    def param_description_and_response_docstring(self, builder: Operation) -> List[str]:
        return self.param_description(builder) + self.response_docstring(builder)

    def _content_type_docstring(self, builder: Operation) -> str:
        content_type_str = (
            f":keyword str content_type: Media type of the body sent to the API. Default value is \"{builder.parameters.default_content_type}\". " +
            "Allowed values are: \"{}.\"".format('", "'.join(builder.parameters.content_types))
        )
        return content_type_str

    def _get_json_response_template_to_status_codes(self, builder: BaseBuilder) -> Dict[str, List[Union[str, int]]]:
        # successful status codes of responses that have bodies
        responses = [
            response for response in builder.responses
            if any(code in builder.success_status_code for code in response.status_codes)
            and isinstance(response.schema, (DictionarySchema, ListSchema, ObjectSchema))
        ]
        retval = defaultdict(list)
        for response in responses:
            status_codes = [str(status_code) for status_code in response.status_codes]
            response_json = _serialize_json_dict(response.schema.get_json_template_representation())
            retval[response_json].extend(status_codes)
        return retval

    def get_example_template(self, builder: BaseBuilder) -> List[str]:
        template = []
        if self._has_json_example_template(builder):
            template.append("")
            template += self._get_json_example_template(builder)
        if self._has_files_example_template(builder):
            template.append("")
            template += self._get_files_example_template(builder)
        if self._get_json_response_template_to_status_codes(builder):
            template.append("")
            template += self._get_json_response_template(builder)
        return template

    def _get_json_example_template(self, builder: BaseBuilder) -> List[str]:
        template = []
        json_body = builder.parameters.json_body
        try:
            discriminator_name = json_body.discriminator_name
        except AttributeError:
            discriminator_name = None
        if discriminator_name:
            template.append(
                "{} = '{}'".format(
                    discriminator_name,
                    "' or '".join(json_body.subtype_map.values())
                )
            )
            template.append("")

        try:
            property_with_discriminator = json_body.property_with_discriminator
        except AttributeError:
            property_with_discriminator = None
        if property_with_discriminator:
            polymorphic_schemas = [
                s for s in self.code_model.sorted_schemas
                if s.name in property_with_discriminator.schema.subtype_map.values()
            ]
            num_schemas = min(
                self.code_model.options['polymorphic_examples'],
                len(polymorphic_schemas)
            )
            for i in range(num_schemas):
                schema = polymorphic_schemas[i]
                polymorphic_property = _serialize_json_dict(
                    schema.get_json_template_representation(),
                )
                template.extend(
                    f"{property_with_discriminator.name} = {polymorphic_property}".splitlines()
                )
                if i != num_schemas - 1:
                    template.append("# OR")
            template.append("")
        template.append("# JSON input template you can fill out and use as your `json` input.")
        json_template = _serialize_json_dict(
            builder.parameters.json_body.get_json_template_representation(),
        )
        template.extend(
            f"{self._json_example_param_name(builder)} = {json_template}".splitlines()
        )
        return template

    def _get_files_example_template(self, builder: BaseBuilder) -> List[str]:
        return [
            "# multipart input template you can fill out and use as your `files` input.",
            f"files = {_serialize_files_dict(builder.parameters._multipart_parameters)}"
        ]

    def _get_json_response_template(self, builder: BaseBuilder) -> List[str]:
        template = []
        for response_body, status_codes in self._get_json_response_template_to_status_codes(builder).items():
            template.append("# response body for status code(s): {}".format(', '.join(status_codes)))
            template.extend(f"response.json() == {response_body}".splitlines())
        return template

    def _serialize_path_format_parameters(self, builder: BaseBuilder) -> List[str]:
        return _serialize_parameters_dict(
            builder.parameters.path,
            dict_name="path_format_arguments",
            value_callable=partial(
                Parameter.build_serialize_data_call,
                function_name="url",
            )
        )

    def pop_kwargs_from_signature(self, builder: Operation) -> List[str]:
        retval = []
        for kwarg in self._get_kwargs_to_pop(builder):
            if kwarg._has_default_value():
                retval.append(
                    f"{kwarg.serialized_name} = kwargs.pop('{kwarg.serialized_name}', " +
                    f"{kwarg.default_value_declaration})  # type: {kwarg.type_annotation}"
                )
            else:
                retval.append(f"{kwarg.serialized_name} = kwargs.pop('{kwarg.serialized_name}')  # type: {kwarg.type_annotation}")
        return retval

############################## REQUEST BUILDERS ##############################

class RequestBuilderBaseSerializer(BuilderBaseSerializer):

    def description_and_summary(self, builder: RequestBuilder) -> List[str]:
        retval = super().description_and_summary(builder)
        retval += [
            "See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.",
            ""
        ]
        return retval

    def want_example_template(self, builder: RequestBuilder) -> bool:
        if builder.parameters.has_body:
            body_kwargs = set(builder.parameters.body_kwarg_names.keys())
            return bool(body_kwargs.intersection({"json", "files"}))
        return bool(self._get_json_response_template_to_status_codes(builder))

    @property
    def _function_definition(self) -> str:
        return "def"

    @property
    def _is_in_class(self) -> bool:
        return False

    def _response_type_annotation(self, builder: RequestBuilder, modify_if_head_as_boolean: bool = True) -> str:
        return "HttpRequest"

    def response_docstring(self, builder: RequestBuilder) -> List[str]:
        core_import = "{}.core.rest".format(
            self.code_model.namespace if self.code_model.options["vendor"] else "azure"
        )
        response_str = (
            f":return: Returns an :class:`~{ core_import }.HttpRequest` that you will pass to the client's " +
            "`send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to " +
            "incorporate this response into your code flow."
        )
        rtype_str = f":rtype: ~{ core_import }.HttpRequest"
        return [response_str, rtype_str]

    def _json_example_param_name(self, builder: RequestBuilder) -> str:
        return "json"

    def _has_json_example_template(self, builder: RequestBuilder) -> bool:
        return "json" in builder.parameters.body_kwarg_names

    def _has_files_example_template(self, builder: RequestBuilder) -> bool:
        return "files" in builder.parameters.body_kwarg_names

class RequestBuilderGenericSerializer(RequestBuilderBaseSerializer):

    @property
    def _want_inline_type_hints(self) -> bool:
        return False

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, _response_type_annotation: str):
        return utils.method_signature_and_response_type_annotation_template(
            async_mode=False,
            method_signature=method_signature,
            response_type_annotation=_response_type_annotation
        )

    def _get_kwargs_to_pop(self, builder: BaseBuilder):
        return builder.parameters.kwargs_to_pop(async_mode=False)

class RequestBuilderPython3Serializer(RequestBuilderBaseSerializer):

    @property
    def _want_inline_type_hints(self) -> bool:
        return True

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, _response_type_annotation: str):
        return utils.method_signature_and_response_type_annotation_template(
            async_mode=True,
            method_signature=method_signature,
            response_type_annotation=_response_type_annotation
        )


    def _get_kwargs_to_pop(self, builder: BaseBuilder):
        return builder.parameters.kwargs_to_pop(async_mode=True)

############################## NORMAL OPERATIONS ##############################

class OperationBaseSerializer(BuilderBaseSerializer):

    def description_and_summary(self, builder: Operation) -> List[str]:
        retval = super().description_and_summary(builder)
        if builder.deprecated:
            retval.append(".. warning::")
            retval.append("    This method is deprecated")
            retval.append("")
        return retval

    @property
    def _is_in_class(self) -> bool:
        return True

    def _response_docstring_type_wrapper(self, builder: BaseBuilder) -> List[str]:
        return []

    def param_description(self, builder: Operation) -> List[str]:
        description_list = super().param_description(builder)
        description_list.append(":keyword callable cls: A custom type or function that will be passed the direct response")
        return description_list

    def _response_docstring_type_template(self, builder: BaseBuilder) -> str:
        retval = "{}"
        for wrapper in self._response_docstring_type_wrapper(builder)[::-1]:
            retval = f"{wrapper}[{retval}]"
        return retval

    def _response_type_annotation(self, builder: Operation, modify_if_head_as_boolean: bool = True) -> str:
        if modify_if_head_as_boolean and builder.request_builder.method == 'head' and self.code_model.options['head_as_boolean']:
            return "bool"
        response_body_annotations: OrderedSet[str] = {}
        for response in [r for r in builder.responses if r.has_body]:
            response_body_annotations[response.operation_type_annotation] = None
        response_str = ", ".join(response_body_annotations.keys()) or "None"
        if len(response_body_annotations) > 1:
            response_str = f"Union[{response_str}]"
        if builder.has_optional_return_type:
            response_str = f"Optional[{response_str}]"
        return response_str

    def cls_type_annotation(self, builder: Operation) -> str:
        return f"# type: ClsType[{self._response_type_annotation(builder, modify_if_head_as_boolean=False)}]"

    def _response_docstring_text_template(self, builder: Operation) -> str:
        return "{}, or the result of cls(response)"

    def response_docstring(self, builder: Operation) -> List[str]:
        responses_with_body = [r for r in builder.responses if r.has_body]
        if builder.request_builder.method == 'head' and self.code_model.options['head_as_boolean']:
            response_docstring_text = "bool"
            rtype = "bool"
        elif responses_with_body:
            response_body_docstring_text: OrderedSet[str] = {
                response.docstring_text: None
                for response in responses_with_body
            }
            response_docstring_text = " or ".join(response_body_docstring_text.keys())
            response_body_docstring_type: OrderedSet[str] = {
                response.docstring_type: None
                for response in responses_with_body
            }
            rtype = ' or '.join(response_body_docstring_type.keys())
            if builder.has_optional_return_type:
                rtype += " or None"
        else:
            response_docstring_text = "None"
            rtype = "None"
        response_str = f":return: {self._response_docstring_text_template(builder).format(response_docstring_text)}"
        rtype_str = f":rtype: {self._response_docstring_type_template(builder).format(rtype)}"
        return [response_str, rtype_str, ":raises: ~azure.core.exceptions.HttpResponseError"]

    def want_example_template(self, builder: BaseBuilder) -> bool:
        # if not self.code_model.no_models:
        #     return False
        return False
        if builder.parameters.has_body:
            body_params = builder.parameters.body
            return any([
                b for b in body_params
                if isinstance(b.schema, (DictionarySchema, ListSchema, ObjectSchema))
            ])
        return bool(self._get_json_response_template_to_status_codes(builder))

    def _json_example_param_name(self, builder: Operation) -> str:
        return builder.parameters.body[0].serialized_name

    def _has_json_example_template(self, builder: BaseBuilder) -> bool:
        return builder.parameters.has_body

    def _has_files_example_template(self, builder: RequestBuilder) -> bool:
        return False

    def _serialize_grouped_parameters(self, builder: Operation) -> List[str]:
        retval = []
        for grouped_parameter in builder.parameters.grouped:
            retval.append(f"{grouped_parameter.serialized_name} = None")
        for grouper_name, grouped_parameters in groupby(builder.parameters.grouped, key=lambda a: a.grouped_by.serialized_name):
            retval.append(f"if {grouper_name} is not None:")
            for grouped_parameter in grouped_parameters:
                retval.append(f"    {grouped_parameter.serialized_name} = {grouper_name}.{grouped_parameter.serialized_name.lstrip('_')}")
        return retval

    def _serialize_body_call(self, builder: Operation, send_xml: bool, ser_ctxt: Optional[str], ser_ctxt_name: str) -> str:
        body_param = builder.parameters.body[0]
        body_is_xml = ", is_xml=True" if send_xml else ""
        pass_ser_ctxt = f", {ser_ctxt_name}={ser_ctxt_name}" if ser_ctxt else ""
        if isinstance(builder, NoModelOperation):
            return f"{builder.serialized_body_kwarg} = self._serialize.body({builder.parameters.body[0].serialized_name}, 'object')"
        return f"{builder.serialized_body_kwarg} = self._serialize.body({body_param.serialized_name}, '{ body_param.serialization_type }'{body_is_xml}{ pass_ser_ctxt })"

    def _serialize_body(self, builder: Operation) -> List[str]:
        retval = []
        send_xml = bool(builder.parameters.has_body and any(["xml" in ct for ct in builder.parameters.content_types]))
        ser_ctxt_name = "serialization_ctxt"
        ser_ctxt = builder.parameters.body[0].xml_serialization_ctxt if send_xml else None
        if ser_ctxt:
            retval.append(f'{ser_ctxt_name} = {{"xml": {{{ser_ctxt}}}}}')
        body_param = builder.parameters.body[0]
        serialize_body_call = self._serialize_body_call(
            builder,
            send_xml,
            ser_ctxt,
            ser_ctxt_name,
        )
        if body_param.required:
            retval.append(serialize_body_call)
        else:
            retval.append(f"if {body_param.serialized_name} is not None:")
            retval.append("    " + serialize_body_call)
            if len(builder.body_kwargs_to_pass_to_request_builder) == 1:
                retval.append("else:")
                retval.append(f"    {builder.serialized_body_kwarg} = None")
        return retval

    def _set_body_content_kwarg(self, builder: Operation, schema_request: SchemaRequest):
        retval = []
        if schema_request.is_stream_request:
            retval.append(f"content = {builder.parameters.body[0].serialized_name}")
        elif schema_request.body_parameter_has_schema and not builder.request_builder.multipart:
            retval.extend(self._serialize_body(builder))
        return retval

    def _content_type_error_check(self, builder: Operation) -> List[str]:
        retval = ["else:"]
        retval.append("    raise ValueError(")
        retval.append("        \"The content_type '{}' is not one of the allowed values: \"")
        retval.append(f"        \"{builder.parameters.content_types}\".format(content_type)")
        retval.append("    )")
        return retval

    def _serialize_body_parameters(
        self,
        builder: Operation,
    ) -> List[str]:
        retval = []
        if len(builder.request_builder.schema_requests) == 1:
            retval.extend(self._set_body_content_kwarg(
                builder, builder.request_builder.schema_requests[0]
            ))
        else:
            for idx, schema_request in enumerate(builder.request_builder.schema_requests):
                if_statement = "if" if idx == 0 else "elif"
                retval.append(f'{if_statement} content_type.split(";")[0] in {schema_request.pre_semicolon_media_types}:')
                retval.extend([
                    "    " + line
                    for line in self._set_body_content_kwarg(
                        builder, schema_request
                    )
                ])
            retval.extend(self._content_type_error_check(builder))

        return retval

    def _serialize_files_parameter(self, builder: Operation) -> List[str]:
        retval = ["files = {"]
        for parameter in builder.parameters.body:
            retval.append(f"    \"{parameter.rest_api_name}\": {parameter.serialized_name},")
        retval.append("}")
        return retval

    def _call_request_builder_helper(
        self,
        builder: Operation,
        request_builder: RequestBuilder,
        template_url: Optional[str] = None,
    ) -> List[str]:
        retval = []
        if len(builder.body_kwargs_to_pass_to_request_builder) > 1:
            for k in builder.body_kwargs_to_pass_to_request_builder:
                retval.append(f"{k} = None")
        if builder.parameters.grouped:
            # request builders don't allow grouped parameters, so we group them before making the call
            retval.extend(self._serialize_grouped_parameters(builder))
        if request_builder.multipart:
            # we have to construct our form data before passing to the request as well
            retval.append("# Construct form data")
            retval.extend(self._serialize_files_parameter(builder))
        if builder.parameters.is_flattened:
            # unflatten before passing to request builder as well
            retval.append(builder.parameters.build_flattened_object())
        # we also don't do constant bodies in request builders
        for constant_body in builder.parameters.constant_bodies:
            retval.append(f"{constant_body.serialized_name} = {constant_body.constant_declaration}")
        if builder.parameters.has_body:
            retval.extend(self._serialize_body_parameters(builder))
        operation_group_name = request_builder.operation_group_name
        request_path_name = "rest{}.{}".format(
            ("_" + operation_group_name) if operation_group_name else "",
            request_builder.name
        )
        retval.append("")
        retval.append(f"request = {request_path_name}(")
        for parameter in request_builder.parameters.method:
            if parameter.is_body:
                continue
            retval.append(f"    {parameter.serialized_name}={parameter.name_in_high_level_operation},")
        if request_builder.parameters.has_body:
            for kwarg in builder.body_kwargs_to_pass_to_request_builder:
                retval.append(f"    {kwarg}={kwarg},")
        template_url = template_url or f"self.{builder.name}.metadata['url']"
        retval.append(f"    template_url={template_url},")
        retval.append(")._to_pipeline_transport_request()")
        if builder.parameters.path:
            retval.extend(self._serialize_path_format_parameters(builder))
        retval.append("request.url = self._client.format_url(request.url{})".format(
            ", **path_format_arguments" if builder.parameters.path else ""
        ))
        return retval

    def call_request_builder(self, builder: Operation) -> List[str]:
        return self._call_request_builder_helper(builder, builder.request_builder)


class SyncOperationSerializer(OperationBaseSerializer):

    @property
    def _want_inline_type_hints(self) -> bool:
        return False

    @property
    def _function_definition(self) -> str:
        return "def"

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, _response_type_annotation: str):
        return utils.method_signature_and_response_type_annotation_template(
            async_mode=False,
            method_signature=method_signature,
            response_type_annotation=_response_type_annotation
        )


    def _get_kwargs_to_pop(self, builder: BaseBuilder):
        return builder.parameters.kwargs_to_pop(async_mode=False)

class AsyncOperationSerializer(OperationBaseSerializer):

    @property
    def _want_inline_type_hints(self) -> bool:
        return True

    @property
    def _function_definition(self) -> str:
        return "async def"

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, _response_type_annotation: str):
        return utils.method_signature_and_response_type_annotation_template(
            async_mode=True,
            method_signature=method_signature,
            response_type_annotation=_response_type_annotation
        )


    def _get_kwargs_to_pop(self, builder: BaseBuilder):
        return builder.parameters.kwargs_to_pop(async_mode=True)

############################## PAGING OPERATIONS ##############################

class PagingOperationBaseSerializer(OperationBaseSerializer):

    def _response_docstring_text_template(self, builder: PagingOperation) -> str:
        return "An iterator like instance of either {} or the result of cls(response)"

    def cls_type_annotation(self, builder: PagingOperation) -> str:
        interior = super()._response_type_annotation(builder, modify_if_head_as_boolean=False)
        return f"# type: ClsType[{interior}]"

    def call_next_link_request_builder(self, builder: PagingOperation) -> List[str]:
        if builder.next_operation:
            request_builder = builder.next_request_builder
            template_url = f"'{request_builder.url}'"
        else:
            request_builder = builder.request_builder
            template_url = "next_link"
        request_builder = builder.next_request_builder or builder.request_builder
        return self._call_request_builder_helper(
            builder,
            request_builder,
            template_url=template_url,
        )


class SyncPagingOperationSerializer(PagingOperationBaseSerializer, SyncOperationSerializer):

    def _response_docstring_type_wrapper(self, builder: PagingOperation) -> List[str]:
        return [f"~{builder.get_pager_path(async_mode=False)}"]

    def _response_type_annotation_wrapper(self, builder: BaseBuilder) -> List[str]:
        return ["Iterable"]

class AsyncPagingOperationSerializer(PagingOperationBaseSerializer, AsyncOperationSerializer):

    def _response_docstring_type_wrapper(self, builder: PagingOperation) -> List[str]:
        return [f"~{builder.get_pager_path(async_mode=True)}"]

    @property
    def _function_definition(self) -> str:
        return "def"

    def _response_type_annotation_wrapper(self, builder: PagingOperation) -> List[str]:
        return ["AsyncIterable"]


############################## LRO OPERATIONS ##############################

class LROOperationBaseSerializer(OperationBaseSerializer):

    def cls_type_annotation(self, builder: LROOperation) -> str:
        return f"# type: ClsType[{super()._response_type_annotation(builder, modify_if_head_as_boolean=False)}]"

    @abstractmethod
    def _default_polling_method(self, builder: LROOperation) -> str:
        ...

    @property
    @abstractmethod
    def _polling_method_type(self):
        ...

    def param_description(self, builder: LROOperation) -> List[str]:
        retval = super().param_description(builder)
        retval.append(":keyword str continuation_token: A continuation token to restart a poller from a saved state.")
        retval.append(
            f":keyword polling: By default, your polling method will be {self._default_polling_method(builder)}. Pass in False for this "
            "operation to not poll, or pass in your own initialized polling object for a personal polling strategy."
        )
        retval.append(f":paramtype polling: bool or ~{self._polling_method_type}")
        retval.append(":keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.")
        return retval

class SyncLROOperationSerializer(LROOperationBaseSerializer, SyncOperationSerializer):

    def _response_docstring_text_template(self, builder: LROOperation) -> str:
        lro_section = f"An instance of {builder.get_poller(async_mode=False)} "
        return lro_section + "that returns either {} or the result of cls(response)"

    def _response_docstring_type_wrapper(self, builder: LROOperation) -> List[str]:
        return [f"~{builder.get_poller_path(async_mode=False)}"]

    def _response_type_annotation_wrapper(self, builder: LROOperation) -> List[str]:
        return [builder.get_poller(async_mode=False)]

    def _default_polling_method(self, builder: LROOperation) -> str:
        return builder.get_default_polling_method(
            async_mode=False, azure_arm=self.code_model.options["azure_arm"]
        )

    @property
    def _polling_method_type(self):
        return "azure.core.polling.PollingMethod"

class AsyncLROOperationSerializer(LROOperationBaseSerializer, AsyncOperationSerializer):

    def _response_docstring_text_template(self, builder: LROOperation) -> str:
        lro_section = f"An instance of {builder.get_poller(async_mode=True)} "
        return lro_section + "that returns either {} or the result of cls(response)"

    def _response_docstring_type_wrapper(self, builder: LROOperation) -> List[str]:
        return [f"~{builder.get_poller_path(async_mode=True)}"]

    def _response_type_annotation_wrapper(self, builder: LROOperation) -> List[str]:
        return [builder.get_poller(async_mode=True)]

    def _default_polling_method(self, builder: LROOperation) -> str:
        return builder.get_default_polling_method(
            async_mode=True, azure_arm=self.code_model.options["azure_arm"]
        )

    @property
    def _polling_method_type(self):
        return "azure.core.polling.AsyncPollingMethod"

############################## LRO PAGING OPERATIONS ##############################

class SyncLROPagingOperationSerializer(SyncLROOperationSerializer, SyncPagingOperationSerializer):

    def _response_docstring_type_wrapper(self, builder: LROPagingOperation) -> List[str]:
        return (
            SyncLROOperationSerializer._response_docstring_type_wrapper(self, builder) +
            SyncPagingOperationSerializer._response_docstring_type_wrapper(self, builder)
        )

    def _response_type_annotation_wrapper(self, builder: LROPagingOperation) -> List[str]:
        return (
            SyncLROOperationSerializer._response_type_annotation_wrapper(self, builder) +
            [builder.get_pager(async_mode=False)]
        )

    def _response_docstring_text_template(self, builder: LROPagingOperation) -> str:
        lro_doc = SyncLROOperationSerializer._response_docstring_text_template(self, builder)
        paging_doc = SyncPagingOperationSerializer._response_docstring_text_template(self, builder)
        paging_doc = paging_doc.replace(paging_doc[0], paging_doc[0].lower(), 1)
        return lro_doc.format(paging_doc).replace(" or the result of cls(response)", "", 1).replace("either ", "", 1)

    def cls_type_annotation(self, builder: LROPagingOperation) -> str:
        return f"# type: ClsType[{self._response_type_annotation(builder, modify_if_head_as_boolean=False)}]"

class AsyncLROPagingOperationSerializer(AsyncLROOperationSerializer, AsyncPagingOperationSerializer):

    @property
    def _function_definition(self) -> str:
        return "async def"

    def _response_docstring_type_wrapper(self, builder: LROPagingOperation) -> List[str]:
        return (
            AsyncLROOperationSerializer._response_docstring_type_wrapper(self, builder) +
            AsyncPagingOperationSerializer._response_docstring_type_wrapper(self, builder)
        )

    def _response_type_annotation_wrapper(self, builder: LROPagingOperation) -> List[str]:
        return (
            AsyncLROOperationSerializer._response_type_annotation_wrapper(self, builder) +
            [builder.get_pager(async_mode=True)]
        )

    def _response_docstring_text_template(self, builder: LROPagingOperation) -> str:
        lro_doc = AsyncLROOperationSerializer._response_docstring_text_template(self, builder)
        paging_doc = AsyncPagingOperationSerializer._response_docstring_text_template(self, builder)
        paging_doc = paging_doc.replace(paging_doc[0], paging_doc[0].lower(), 1)
        return lro_doc.format(paging_doc).replace(" or the result of cls(response)", "", 1).replace("either ", "", 1)
