# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar, cast

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

from ..._operations._operations import (
    build_get_array_request,
    build_get_object_request,
    build_get_string_request,
    build_put_array_request,
    build_put_object_request,
    build_put_string_request,
)
from .._vendor import MixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AnythingClientOperationsMixin(MixinABC):
    @distributed_trace_async
    async def get_object(self, **kwargs: Any) -> Any:
        """Basic get that returns an object as anything. Returns object { 'message': 'An object was
        successfully returned' }.

        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[Any]

        request = build_get_object_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(Any, deserialized), {})

        return cast(Any, deserialized)

    @distributed_trace_async
    async def put_object(self, input: Any, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Basic put that puts an object as anything. Pass in {'foo': 'bar'} to get a 200 and anything
        else to get an object error.

        :param input: Pass in {'foo': 'bar'} for a 200, anything else for an object error. Required.
        :type input: any
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = input

        request = build_put_object_request(
            content_type=content_type,
            json=_json,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def get_string(self, **kwargs: Any) -> Any:
        """Basic get that returns an string as anything. Returns string 'foo'.

        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[Any]

        request = build_get_string_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(Any, deserialized), {})

        return cast(Any, deserialized)

    @distributed_trace_async
    async def put_string(self, input: Any, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Basic put that puts an string as anything. Pass in 'anything' to get a 200 and anything else to
        get an object error.

        :param input: Pass in 'anything' for a 200, anything else for an object error. Required.
        :type input: any
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = input

        request = build_put_string_request(
            content_type=content_type,
            json=_json,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def get_array(self, **kwargs: Any) -> Any:
        """Basic get that returns an array as anything. Returns string ['foo', 'bar'].

        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[Any]

        request = build_get_array_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(Any, deserialized), {})

        return cast(Any, deserialized)

    @distributed_trace_async
    async def put_array(self, input: Any, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Basic put that puts an array as anything. Pass in ['foo', 'bar'] to get a 200 and anything else
        to get an object error.

        :param input: Pass in ['foo', 'bar'] for a 200, anything else for an object error. Required.
        :type input: any
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = input

        request = build_put_array_request(
            content_type=content_type,
            json=_json,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
