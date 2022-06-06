# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, IO, Optional, Union, overload

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

@overload
def build_analyze_body_request(
    *,
    content_type: Optional[str] = None,
    json: Optional[JSON] = None,
    **kwargs: Any
) -> HttpRequest:
    """Analyze body, that could be different media types.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Input parameter. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "source": "str"  # Optional. File source path.
            }
    """


@overload
def build_analyze_body_request(
    *,
    content_type: Optional[str] = None,
    content: Optional[IO] = None,
    **kwargs: Any
) -> HttpRequest:
    """Analyze body, that could be different media types.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Input parameter. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_analyze_body_request(
    **kwargs: Any
) -> HttpRequest:
    """Analyze body, that could be different media types.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json',
     'application/pdf', 'image/jpeg', 'image/png', 'image/tiff'. Default value is None.
    :paramtype content_type: str
    :keyword json: Input parameter. Is either a model type or a IO type. Default value is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/mediatypes/analyze"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_analyze_body_no_accept_header_request(
    *,
    content_type: Optional[str] = None,
    json: Optional[JSON] = None,
    **kwargs: Any
) -> HttpRequest:
    """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
    type.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Input parameter. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "source": "str"  # Optional. File source path.
            }
    """


@overload
def build_analyze_body_no_accept_header_request(
    *,
    content_type: Optional[str] = None,
    content: Optional[IO] = None,
    **kwargs: Any
) -> HttpRequest:
    """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
    type.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Input parameter. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_analyze_body_no_accept_header_request(
    **kwargs: Any
) -> HttpRequest:
    """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
    type.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json',
     'application/pdf', 'image/jpeg', 'image/png', 'image/tiff'. Default value is None.
    :paramtype content_type: str
    :keyword json: Input parameter. Is either a model type or a IO type. Default value is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    # Construct URL
    _url = "/mediatypes/analyzeNoAccept"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_content_type_with_encoding_request(
    *,
    content: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Pass in contentType 'text/plain; charset=UTF-8' to pass test. Value for input does not matter.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content: Input parameter. Default value is None.
    :paramtype content: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/mediatypes/contentTypeWithEncoding"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        content=content,
        **kwargs
    )


def build_binary_body_with_two_content_types_request(
    *,
    content: IO,
    **kwargs: Any
) -> HttpRequest:
    """Binary body with two content types. Pass in of {'hello': 'world'} for the application/json
    content type, and a byte stream of 'hello, world!' for application/octet-stream.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content: The payload body. Required.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "text/plain")

    # Construct URL
    _url = "/mediatypes/binaryBodyTwoContentTypes"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        content=content,
        **kwargs
    )


def build_binary_body_with_three_content_types_request(
    *,
    content: IO,
    **kwargs: Any
) -> HttpRequest:
    """Binary body with three content types. Pass in string 'hello, world' with content type
    'text/plain', {'hello': world'} with content type 'application/json' and a byte string for
    'application/octet-stream'.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content: The payload body. Required.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "text/plain")

    # Construct URL
    _url = "/mediatypes/binaryBodyThreeContentTypes"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        content=content,
        **kwargs
    )


def build_put_text_and_json_body_request(
    *,
    content: str,
    **kwargs: Any
) -> HttpRequest:
    """Body that's either text/plain or application/json.

    See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this request
    builder into your code flow.

    :keyword content: The payload body. Required.
    :paramtype content: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "text/plain")

    # Construct URL
    _url = "/mediatypes/textAndJson"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        content=content,
        **kwargs
    )
