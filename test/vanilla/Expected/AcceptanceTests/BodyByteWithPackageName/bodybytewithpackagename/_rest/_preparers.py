# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

_SERIALIZER = Serializer()


def prepare_byte_get_null(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get null byte value.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/byte/null")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_byte_get_empty(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get empty byte value ''.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/byte/empty")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_byte_get_non_ascii(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/byte/nonAscii")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_byte_put_non_ascii(
    byte_body,  # type: bytearray
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param byte_body: Base64-encoded non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).
    :type byte_body: bytearray
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/byte/nonAscii")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = byte_body

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **body_content_kwargs)


def prepare_byte_get_invalid(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get invalid byte value ':::SWAGGER::::'.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/byte/invalid")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )