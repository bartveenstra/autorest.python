# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class StringOperations(object):
    """StringOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodystring.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _get_null_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = self._get_null_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_null_request.metadata = {"url": "/string/null"}  # type: ignore

    @distributed_trace
    def get_null(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Optional[str]
        """Get null string value value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or None, or the result of cls(response)
        :rtype: str or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[str]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_null_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null.metadata = {"url": "/string/null"}  # type: ignore

    def _put_null_request(
        self,
        body=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._put_null_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, "str")
        else:
            body_content = None
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_null_request.metadata = {"url": "/string/null"}  # type: ignore

    @distributed_trace
    def put_null(
        self,
        string_body=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Set string value null.

        :param string_body: string body.
        :type string_body: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_null_request(body=body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_null.metadata = {"url": "/string/null"}  # type: ignore

    def _get_empty_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = self._get_empty_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_empty_request.metadata = {"url": "/string/empty"}  # type: ignore

    @distributed_trace
    def get_empty(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> str
        """Get empty string value value ''.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_empty_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_empty.metadata = {"url": "/string/empty"}  # type: ignore

    def _put_empty_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        content_type = kwargs.pop("content_type", "application/json")
        body = ""
        accept = "application/json"

        # Construct URL
        url = self._put_empty_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "str")
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_empty_request.metadata = {"url": "/string/empty"}  # type: ignore

    @distributed_trace
    def put_empty(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Set string value empty ''.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_empty_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_empty.metadata = {"url": "/string/empty"}  # type: ignore

    def _get_mbcs_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = self._get_mbcs_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_mbcs_request.metadata = {"url": "/string/mbcs"}  # type: ignore

    @distributed_trace
    def get_mbcs(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> str
        """Get mbcs string value '啊齄丂狛狜隣郎隣兀﨩ˊ〞〡￤℡㈱‐ー﹡﹢﹫、〓ⅰⅹ⒈€㈠㈩ⅠⅫ！￣ぁんァヶΑ︴АЯаяāɡㄅㄩ─╋︵﹄︻︱︳︴ⅰⅹɑɡ〇〾⿻⺁䜣€'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_mbcs_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_mbcs.metadata = {"url": "/string/mbcs"}  # type: ignore

    def _put_mbcs_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        content_type = kwargs.pop("content_type", "application/json")
        body = "啊齄丂狛狜隣郎隣兀﨩ˊ〞〡￤℡㈱‐ー﹡﹢﹫、〓ⅰⅹ⒈€㈠㈩ⅠⅫ！￣ぁんァヶΑ︴АЯаяāɡㄅㄩ─╋︵﹄︻︱︳︴ⅰⅹɑɡ〇〾⿻⺁䜣€"
        accept = "application/json"

        # Construct URL
        url = self._put_mbcs_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "str")
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_mbcs_request.metadata = {"url": "/string/mbcs"}  # type: ignore

    @distributed_trace
    def put_mbcs(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Set string value mbcs '啊齄丂狛狜隣郎隣兀﨩ˊ〞〡￤℡㈱‐ー﹡﹢﹫、〓ⅰⅹ⒈€㈠㈩ⅠⅫ！￣ぁんァヶΑ︴АЯаяāɡㄅㄩ─╋︵﹄︻︱︳︴ⅰⅹɑɡ〇〾⿻⺁䜣€'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_mbcs_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_mbcs.metadata = {"url": "/string/mbcs"}  # type: ignore

    def _get_whitespace_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = self._get_whitespace_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_whitespace_request.metadata = {"url": "/string/whitespace"}  # type: ignore

    @distributed_trace
    def get_whitespace(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> str
        """Get string value with leading and trailing whitespace
        ':code:`<tab>`:code:`<space>`:code:`<space>`Now is the time for all good men to come to the aid
        of their country:code:`<tab>`:code:`<space>`:code:`<space>`'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_whitespace_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_whitespace.metadata = {"url": "/string/whitespace"}  # type: ignore

    def _put_whitespace_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        content_type = kwargs.pop("content_type", "application/json")
        body = "    Now is the time for all good men to come to the aid of their country    "
        accept = "application/json"

        # Construct URL
        url = self._put_whitespace_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "str")
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_whitespace_request.metadata = {"url": "/string/whitespace"}  # type: ignore

    @distributed_trace
    def put_whitespace(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Set String value with leading and trailing whitespace
        ':code:`<tab>`:code:`<space>`:code:`<space>`Now is the time for all good men to come to the aid
        of their country:code:`<tab>`:code:`<space>`:code:`<space>`'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_whitespace_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_whitespace.metadata = {"url": "/string/whitespace"}  # type: ignore

    def _get_not_provided_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = self._get_not_provided_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_not_provided_request.metadata = {"url": "/string/notProvided"}  # type: ignore

    @distributed_trace
    def get_not_provided(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> str
        """Get String value when no string value is sent in response payload.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_not_provided_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_not_provided.metadata = {"url": "/string/notProvided"}  # type: ignore

    def _get_base64_encoded_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = self._get_base64_encoded_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_base64_encoded_request.metadata = {"url": "/string/base64Encoding"}  # type: ignore

    @distributed_trace
    def get_base64_encoded(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> bytearray
        """Get value that is base64 encoded.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bytearray, or the result of cls(response)
        :rtype: bytearray
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bytearray]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_base64_encoded_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("bytearray", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_base64_encoded.metadata = {"url": "/string/base64Encoding"}  # type: ignore

    def _get_base64_url_encoded_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = self._get_base64_url_encoded_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_base64_url_encoded_request.metadata = {"url": "/string/base64UrlEncoding"}  # type: ignore

    @distributed_trace
    def get_base64_url_encoded(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> bytes
        """Get value that is base64url encoded.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bytes, or the result of cls(response)
        :rtype: bytes
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[bytes]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_base64_url_encoded_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("base64", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_base64_url_encoded.metadata = {"url": "/string/base64UrlEncoding"}  # type: ignore

    def _put_base64_url_encoded_request(
        self,
        body,  # type: bytes
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._put_base64_url_encoded_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "base64")
        body_content_kwargs["content"] = body_content
        return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

    _put_base64_url_encoded_request.metadata = {"url": "/string/base64UrlEncoding"}  # type: ignore

    @distributed_trace
    def put_base64_url_encoded(
        self,
        string_body,  # type: bytes
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put value that is base64url encoded.

        :param string_body: string body.
        :type string_body: bytes
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._put_base64_url_encoded_request(body=body, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_base64_url_encoded.metadata = {"url": "/string/base64UrlEncoding"}  # type: ignore

    def _get_null_base64_url_encoded_request(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest
        accept = "application/json"

        # Construct URL
        url = self._get_null_base64_url_encoded_request.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

        return self._client.get(url, query_parameters, header_parameters)

    _get_null_base64_url_encoded_request.metadata = {"url": "/string/nullBase64UrlEncoding"}  # type: ignore

    @distributed_trace
    def get_null_base64_url_encoded(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Optional[bytes]
        """Get null value that is expected to be base64url encoded.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: bytes or None, or the result of cls(response)
        :rtype: bytes or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[bytes]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._get_null_base64_url_encoded_request(**kwargs)

        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("base64", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_null_base64_url_encoded.metadata = {"url": "/string/nullBase64UrlEncoding"}  # type: ignore
