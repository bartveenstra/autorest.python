# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import IO, Optional, TYPE_CHECKING, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_create_ap_true_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/additionalProperties/true")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_create_cat_ap_true_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/additionalProperties/true-subclass")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_create_ap_object_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/additionalProperties/type/object")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_create_ap_string_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/additionalProperties/type/string")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_create_ap_in_properties_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/additionalProperties/in/properties")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_create_ap_in_properties_with_ap_string_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/additionalProperties/in/properties/with/additionalProperties/string")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )

# fmt: on
class PetsOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~additionalproperties.AdditionalPropertiesClient`'s
        :attr:`pets` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def create_ap_true(
        self,
        create_parameters,  # type: _models.PetAPTrue
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPTrue
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPTrue
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_ap_true(
        self,
        create_parameters,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPTrue
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_ap_true(
        self,
        create_parameters,  # type: Union[_models.PetAPTrue, IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPTrue
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a model type or a IO type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPTrue or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PetAPTrue]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IO, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPTrue")

        request = build_create_ap_true_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_ap_true.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPTrue", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_true.metadata = {"url": "/additionalProperties/true"}  # type: ignore

    @overload
    def create_cat_ap_true(
        self,
        create_parameters,  # type: _models.CatAPTrue
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.CatAPTrue
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.CatAPTrue
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CatAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_cat_ap_true(
        self,
        create_parameters,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.CatAPTrue
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CatAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_cat_ap_true(
        self,
        create_parameters,  # type: Union[_models.CatAPTrue, IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.CatAPTrue
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Is either a model type or a IO type. Required.
        :type create_parameters: ~additionalproperties.models.CatAPTrue or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CatAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CatAPTrue]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IO, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "CatAPTrue")

        request = build_create_cat_ap_true_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_cat_ap_true.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("CatAPTrue", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_cat_ap_true.metadata = {"url": "/additionalProperties/true-subclass"}  # type: ignore

    @overload
    def create_ap_object(
        self,
        create_parameters,  # type: _models.PetAPObject
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPObject
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPObject
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPObject or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_ap_object(
        self,
        create_parameters,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPObject
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPObject or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_ap_object(
        self,
        create_parameters,  # type: Union[_models.PetAPObject, IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPObject
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a model type or a IO type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPObject or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPObject or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PetAPObject]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IO, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPObject")

        request = build_create_ap_object_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_ap_object.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPObject", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_object.metadata = {"url": "/additionalProperties/type/object"}  # type: ignore

    @overload
    def create_ap_string(
        self,
        create_parameters,  # type: _models.PetAPString
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPString
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPString
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_ap_string(
        self,
        create_parameters,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPString
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_ap_string(
        self,
        create_parameters,  # type: Union[_models.PetAPString, IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPString
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a model type or a IO type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPString or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PetAPString]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IO, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPString")

        request = build_create_ap_string_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_ap_string.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPString", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_string.metadata = {"url": "/additionalProperties/type/string"}  # type: ignore

    @overload
    def create_ap_in_properties(
        self,
        create_parameters,  # type: _models.PetAPInProperties
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPInProperties
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPInProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInProperties or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_ap_in_properties(
        self,
        create_parameters,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPInProperties
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInProperties or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_ap_in_properties(
        self,
        create_parameters,  # type: Union[_models.PetAPInProperties, IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPInProperties
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a model type or a IO type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPInProperties or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInProperties or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PetAPInProperties]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IO, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPInProperties")

        request = build_create_ap_in_properties_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_ap_in_properties.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPInProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_in_properties.metadata = {"url": "/additionalProperties/in/properties"}  # type: ignore

    @overload
    def create_ap_in_properties_with_ap_string(
        self,
        create_parameters,  # type: _models.PetAPInPropertiesWithAPString
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPInPropertiesWithAPString
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInPropertiesWithAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_ap_in_properties_with_ap_string(
        self,
        create_parameters,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPInPropertiesWithAPString
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInPropertiesWithAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_ap_in_properties_with_ap_string(
        self,
        create_parameters,  # type: Union[_models.PetAPInPropertiesWithAPString, IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.PetAPInPropertiesWithAPString
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a model type or a IO type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPInPropertiesWithAPString or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAPInPropertiesWithAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.PetAPInPropertiesWithAPString]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IO, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPInPropertiesWithAPString")

        request = build_create_ap_in_properties_with_ap_string_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_ap_in_properties_with_ap_string.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPInPropertiesWithAPString", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_ap_in_properties_with_ap_string.metadata = {"url": "/additionalProperties/in/properties/with/additionalProperties/string"}  # type: ignore
