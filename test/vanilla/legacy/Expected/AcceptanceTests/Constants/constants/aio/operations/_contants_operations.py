# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar, Union

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
from ...operations._contants_operations import (
    build_put_client_constants_request,
    build_put_model_as_string_no_required_one_value_default_request,
    build_put_model_as_string_no_required_one_value_no_default_request,
    build_put_model_as_string_no_required_two_value_default_request,
    build_put_model_as_string_no_required_two_value_no_default_request,
    build_put_model_as_string_required_one_value_default_request,
    build_put_model_as_string_required_one_value_no_default_request,
    build_put_model_as_string_required_two_value_default_request,
    build_put_model_as_string_required_two_value_no_default_request,
    build_put_no_model_as_string_no_required_one_value_default_request,
    build_put_no_model_as_string_no_required_one_value_no_default_request,
    build_put_no_model_as_string_no_required_two_value_default_request,
    build_put_no_model_as_string_no_required_two_value_no_default_request,
    build_put_no_model_as_string_required_one_value_default_request,
    build_put_no_model_as_string_required_one_value_no_default_request,
    build_put_no_model_as_string_required_two_value_default_request,
    build_put_no_model_as_string_required_two_value_no_default_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ContantsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~constants.aio.AutoRestSwaggerConstantService`'s
        :attr:`contants` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def put_no_model_as_string_no_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self,
        input: Optional[Union[str, "_models.NoModelAsStringNoRequiredTwoValueNoDefaultOpEnum"]] = None,
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:  Default value is None.
        :type input: str or ~constants.models.NoModelAsStringNoRequiredTwoValueNoDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_no_model_as_string_no_required_two_value_no_default_request(
            input=input,
            template_url=self.put_no_model_as_string_no_required_two_value_no_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_no_required_two_value_no_default.metadata = {"url": "/constants/putNoModelAsStringNoRequiredTwoValueNoDefault"}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_no_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self,
        input: Optional[Union[str, "_models.NoModelAsStringNoRequiredTwoValueDefaultOpEnum"]] = "value1",
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:  Default value is "value1".
        :type input: str or ~constants.models.NoModelAsStringNoRequiredTwoValueDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_no_model_as_string_no_required_two_value_default_request(
            input=input,
            template_url=self.put_no_model_as_string_no_required_two_value_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_no_required_two_value_default.metadata = {"url": "/constants/putNoModelAsStringNoRequiredTwoValueDefault"}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_no_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, input: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: Known values are "value1" or None. Default value is "value1".
        :type input: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_no_model_as_string_no_required_one_value_no_default_request(
            input=input,
            template_url=self.put_no_model_as_string_no_required_one_value_no_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_no_required_one_value_no_default.metadata = {"url": "/constants/putNoModelAsStringNoRequiredOneValueNoDefault"}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_no_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, input: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input: Known values are "value1" or None. Default value is "value1".
        :type input: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_no_model_as_string_no_required_one_value_default_request(
            input=input,
            template_url=self.put_no_model_as_string_no_required_one_value_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_no_required_one_value_default.metadata = {"url": "/constants/putNoModelAsStringNoRequiredOneValueDefault"}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, "_models.NoModelAsStringRequiredTwoValueNoDefaultOpEnum"], **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.NoModelAsStringRequiredTwoValueNoDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_no_model_as_string_required_two_value_no_default_request(
            input=input,
            template_url=self.put_no_model_as_string_required_two_value_no_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_required_two_value_no_default.metadata = {"url": "/constants/putNoModelAsStringRequiredTwoValueNoDefault"}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, "_models.NoModelAsStringRequiredTwoValueDefaultOpEnum"] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:  Default value is "value1".
        :type input: str or ~constants.models.NoModelAsStringRequiredTwoValueDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_no_model_as_string_required_two_value_default_request(
            input=input,
            template_url=self.put_no_model_as_string_required_two_value_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_required_two_value_default.metadata = {"url": "/constants/putNoModelAsStringRequiredTwoValueDefault"}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input:  Default value is "value1". Note that overriding this default value may result
         in unsupported behavior.
        :paramtype input: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        input = kwargs.pop("input", _params.pop("input", "value1"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_no_model_as_string_required_one_value_no_default_request(
            input=input,
            template_url=self.put_no_model_as_string_required_one_value_no_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_required_one_value_no_default.metadata = {"url": "/constants/putNoModelAsStringRequiredOneValueNoDefault"}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword input:  Default value is "value1". Note that overriding this default value may result
         in unsupported behavior.
        :paramtype input: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        input = kwargs.pop("input", _params.pop("input", "value1"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_no_model_as_string_required_one_value_default_request(
            input=input,
            template_url=self.put_no_model_as_string_required_one_value_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_required_one_value_default.metadata = {"url": "/constants/putNoModelAsStringRequiredOneValueDefault"}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_no_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self,
        input: Optional[Union[str, "_models.ModelAsStringNoRequiredTwoValueNoDefaultOpEnum"]] = None,
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:  Default value is None.
        :type input: str or ~constants.models.ModelAsStringNoRequiredTwoValueNoDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_model_as_string_no_required_two_value_no_default_request(
            input=input,
            template_url=self.put_model_as_string_no_required_two_value_no_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_no_required_two_value_no_default.metadata = {"url": "/constants/putModelAsStringNoRequiredTwoValueNoDefault"}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_no_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self,
        input: Optional[Union[str, "_models.ModelAsStringNoRequiredTwoValueDefaultOpEnum"]] = "value1",
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:  Default value is "value1".
        :type input: str or ~constants.models.ModelAsStringNoRequiredTwoValueDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_model_as_string_no_required_two_value_default_request(
            input=input,
            template_url=self.put_model_as_string_no_required_two_value_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_no_required_two_value_default.metadata = {"url": "/constants/putModelAsStringNoRequiredTwoValueDefault"}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_no_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self,
        input: Optional[Union[str, "_models.ModelAsStringNoRequiredOneValueNoDefaultOpEnum"]] = None,
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:  Default value is None.
        :type input: str or ~constants.models.ModelAsStringNoRequiredOneValueNoDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_model_as_string_no_required_one_value_no_default_request(
            input=input,
            template_url=self.put_model_as_string_no_required_one_value_no_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_no_required_one_value_no_default.metadata = {"url": "/constants/putModelAsStringNoRequiredOneValueNoDefault"}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_no_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self,
        input: Optional[Union[str, "_models.ModelAsStringNoRequiredOneValueDefaultOpEnum"]] = "value1",
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:  Default value is "value1".
        :type input: str or ~constants.models.ModelAsStringNoRequiredOneValueDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_model_as_string_no_required_one_value_default_request(
            input=input,
            template_url=self.put_model_as_string_no_required_one_value_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_no_required_one_value_default.metadata = {"url": "/constants/putModelAsStringNoRequiredOneValueDefault"}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_required_two_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, "_models.ModelAsStringRequiredTwoValueNoDefaultOpEnum"], **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.ModelAsStringRequiredTwoValueNoDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_model_as_string_required_two_value_no_default_request(
            input=input,
            template_url=self.put_model_as_string_required_two_value_no_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_required_two_value_no_default.metadata = {"url": "/constants/putModelAsStringRequiredTwoValueNoDefault"}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_required_two_value_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, "_models.ModelAsStringRequiredTwoValueDefaultOpEnum"] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:  Default value is "value1".
        :type input: str or ~constants.models.ModelAsStringRequiredTwoValueDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_model_as_string_required_two_value_default_request(
            input=input,
            template_url=self.put_model_as_string_required_two_value_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_required_two_value_default.metadata = {"url": "/constants/putModelAsStringRequiredTwoValueDefault"}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_required_one_value_no_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, "_models.ModelAsStringRequiredOneValueNoDefaultOpEnum"], **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.ModelAsStringRequiredOneValueNoDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_model_as_string_required_one_value_no_default_request(
            input=input,
            template_url=self.put_model_as_string_required_one_value_no_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_required_one_value_no_default.metadata = {"url": "/constants/putModelAsStringRequiredOneValueNoDefault"}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_required_one_value_default(  # pylint: disable=inconsistent-return-statements
        self, input: Union[str, "_models.ModelAsStringRequiredOneValueDefaultOpEnum"] = "value1", **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:  Default value is "value1".
        :type input: str or ~constants.models.ModelAsStringRequiredOneValueDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_model_as_string_required_one_value_default_request(
            input=input,
            template_url=self.put_model_as_string_required_one_value_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_required_one_value_default.metadata = {"url": "/constants/putModelAsStringRequiredOneValueDefault"}  # type: ignore

    @distributed_trace_async
    async def put_client_constants(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Pass constants from the client to this function. Will pass in constant path, query, and header
        parameters.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_put_client_constants_request(
            header_constant=self._config.header_constant,
            query_constant=self._config.query_constant,
            path_constant=self._config.path_constant,
            template_url=self.put_client_constants.metadata["url"],
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

        if cls:
            return cls(pipeline_response, None, {})

    put_client_constants.metadata = {"url": "/constants/clientConstants/{path-constant}"}  # type: ignore
