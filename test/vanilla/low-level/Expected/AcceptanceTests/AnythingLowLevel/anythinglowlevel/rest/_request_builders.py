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
    from typing import Any, Optional

_SERIALIZER = Serializer()


def build_get_object_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Basic get that returns an object as anything. Returns object { 'message': 'An object was
    successfully returned' }.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/anything/object")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_object_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Basic put that puts an object as anything. Pass in {'foo': 'bar'} to get a 200 and anything
    else to get an object error.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Pass in {'foo': 'bar'} for a 200, anything else for an
     object error.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Pass in {'foo': 'bar'} for a 200, anything else for an
     object error.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "Any (optional)"
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", "/anything/object")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_get_string_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Basic get that returns an string as anything. Returns string 'foo'.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/anything/string")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_string_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Basic put that puts an string as anything. Pass in 'anything' to get a 200 and anything else to
    get an object error.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Pass in 'anything' for a 200, anything else for an object
     error.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Pass in 'anything' for a 200, anything else for an object
     error.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "Any (optional)"
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", "/anything/string")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)


def build_get_array_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Basic get that returns an array as anything. Returns string ['foo', 'bar'].

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/anything/array")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


def build_put_array_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Basic put that puts an array as anything. Pass in ['foo', 'bar'] to get a 200 and anything else
    to get an object error.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Pass in ['foo', 'bar'] for a 200, anything else for an
     object error.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Pass in ['foo', 'bar'] for a 200, anything else for an
     object error.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = "Any (optional)"
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", "/anything/array")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **kwargs)