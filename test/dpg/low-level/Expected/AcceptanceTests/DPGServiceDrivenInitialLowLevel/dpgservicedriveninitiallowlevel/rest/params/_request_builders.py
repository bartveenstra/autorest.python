# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..._serialization import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    if sys.version_info >= (3, 9):
        from collections.abc import MutableMapping
    else:
        from typing import MutableMapping  # type: ignore
    JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_head_no_params_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Head request, no params.
     Initially has no query parameters. After evolution, a new optional query parameter is added.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/serviceDriven/parameters"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="HEAD",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_required_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get true Boolean value on path.
     Initially only has one required Query Parameter. After evolution, a new optional query
    parameter is added.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword parameter: I am a required parameter.
    :paramtype parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    parameter = kwargs.pop('parameter')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/serviceDriven/parameters"

    # Construct parameters
    _params['parameter'] = _SERIALIZER.query("parameter", parameter, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_put_required_optional_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Initially has one required query parameter and one optional query parameter.  After evolution,
    a new optional query parameter is added.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword required_param: I am a required parameter.
    :paramtype required_param: str
    :keyword optional_param: I am an optional parameter. Default value is None.
    :paramtype optional_param: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    required_param = kwargs.pop('required_param')  # type: str
    optional_param = kwargs.pop('optional_param', _params.pop('optionalParam', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/serviceDriven/parameters"

    # Construct parameters
    _params['requiredParam'] = _SERIALIZER.query("required_param", required_param, 'str')
    if optional_param is not None:
        _params['optionalParam'] = _SERIALIZER.query("optional_param", optional_param, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_post_parameters_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """POST a JSON.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. I am a body parameter. My only valid JSON entry is { url:
     "http://example.org/myimage.jpeg" }. Default value is None.
    :paramtype json: JSON
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). I am a body parameter. My only valid JSON entry is { url:
     "http://example.org/myimage.jpeg" }. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "url": "str"  # Required.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/serviceDriven/parameters"

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


def build_get_optional_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get true Boolean value on path.
     Initially has one optional query parameter. After evolution, a new optional query parameter is
    added.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword optional_param: I am an optional parameter. Default value is None.
    :paramtype optional_param: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    optional_param = kwargs.pop('optional_param', _params.pop('optionalParam', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/serviceDriven/moreParameters"

    # Construct parameters
    if optional_param is not None:
        _params['optionalParam'] = _SERIALIZER.query("optional_param", optional_param, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )
