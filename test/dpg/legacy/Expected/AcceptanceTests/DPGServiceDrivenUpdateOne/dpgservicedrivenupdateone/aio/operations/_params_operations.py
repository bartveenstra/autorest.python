# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._params_operations import (
    build_delete_parameters_request,
    build_get_new_operation_request,
    build_get_optional_request,
    build_get_required_request,
    build_head_no_params_request,
    build_post_parameters_request,
    build_put_required_optional_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ParamsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~dpgservicedrivenupdateone.aio.DPGClient`'s
        :attr:`params` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def head_no_params(self, new_parameter: Optional[str] = None, **kwargs: Any) -> JSON:
        """Head request, no params. Initially has no query parameters. After evolution, a new optional
        query parameter is added.

        :param new_parameter: I'm a new input optional parameter. Default value is None.
        :type new_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_head_no_params_request(
            new_parameter=new_parameter,
            template_url=self.head_no_params.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    head_no_params.metadata = {"url": "/serviceDriven/parameters"}  # type: ignore

    @distributed_trace_async
    async def get_required(self, parameter: str, new_parameter: Optional[str] = None, **kwargs: Any) -> JSON:
        """Get true Boolean value on path.
         Initially only has one required Query Parameter. After evolution, a new optional query
        parameter is added.

        :param parameter: I am a required parameter. Required.
        :type parameter: str
        :param new_parameter: I'm a new input optional parameter. Default value is None.
        :type new_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_get_required_request(
            parameter=parameter,
            new_parameter=new_parameter,
            template_url=self.get_required.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_required.metadata = {"url": "/serviceDriven/parameters"}  # type: ignore

    @distributed_trace_async
    async def put_required_optional(
        self,
        required_param: str,
        optional_param: Optional[str] = None,
        new_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> JSON:
        """Initially has one required query parameter and one optional query parameter.  After evolution,
        a new optional query parameter is added.

        :param required_param: I am a required parameter. Required.
        :type required_param: str
        :param optional_param: I am an optional parameter. Default value is None.
        :type optional_param: str
        :param new_parameter: I'm a new input optional parameter. Default value is None.
        :type new_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_put_required_optional_request(
            required_param=required_param,
            optional_param=optional_param,
            new_parameter=new_parameter,
            template_url=self.put_required_optional.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_required_optional.metadata = {"url": "/serviceDriven/parameters"}  # type: ignore

    @overload
    async def post_parameters(
        self, parameter: _models.PostInput, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """POST a JSON or a JPEG.

        :param parameter: I am a body parameter with a new content type. My only valid JSON entry is {
         url: "http://example.org/myimage.jpeg" }. Required.
        :type parameter: ~dpgservicedrivenupdateone.models.PostInput
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def post_parameters(self, parameter: IO, *, content_type: Optional[str] = None, **kwargs: Any) -> JSON:
        """POST a JSON or a JPEG.

        :param parameter: I am a body parameter with a new content type. My only valid JSON entry is {
         url: "http://example.org/myimage.jpeg" }. Required.
        :type parameter: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def post_parameters(self, parameter: Union[_models.PostInput, IO], **kwargs: Any) -> JSON:
        """POST a JSON or a JPEG.

        :param parameter: I am a body parameter with a new content type. My only valid JSON entry is {
         url: "http://example.org/myimage.jpeg" }. Is either a model type or a IO type. Required.
        :type parameter: ~dpgservicedrivenupdateone.models.PostInput or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json',
         'image/jpeg'. Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        _json = None
        _content = None
        if isinstance(parameter, (IO, bytes)):
            _content = parameter
        else:
            _json = self._serialize.body(parameter, "PostInput")
            content_type = content_type or "application/json"

        request = build_post_parameters_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.post_parameters.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    post_parameters.metadata = {"url": "/serviceDriven/parameters"}  # type: ignore

    @distributed_trace_async
    async def delete_parameters(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Delete something.
         Initially the path exists but there is no delete method. After evolution this is a new method
        in a known path.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_parameters_request(
            template_url=self.delete_parameters.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    delete_parameters.metadata = {"url": "/serviceDriven/parameters"}  # type: ignore

    @distributed_trace_async
    async def get_optional(
        self, optional_param: Optional[str] = None, new_parameter: Optional[str] = None, **kwargs: Any
    ) -> JSON:
        """Get true Boolean value on path.
         Initially has one optional query parameter. After evolution, a new optional query parameter is
        added.

        :param optional_param: I am an optional parameter. Default value is None.
        :type optional_param: str
        :param new_parameter: I'm a new input optional parameter. Default value is None.
        :type new_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_get_optional_request(
            optional_param=optional_param,
            new_parameter=new_parameter,
            template_url=self.get_optional.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_optional.metadata = {"url": "/serviceDriven/moreParameters"}  # type: ignore

    @distributed_trace_async
    async def get_new_operation(self, **kwargs: Any) -> JSON:
        """I'm a new operation.
         Initiallty neither path or method exist for this operation. After evolution, this is a new
        method in a new path.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JSON or the result of cls(response)
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_get_new_operation_request(
            template_url=self.get_new_operation.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("object", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_new_operation.metadata = {"url": "/serviceDriven/newPath"}  # type: ignore