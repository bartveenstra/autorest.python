# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, IO, Optional, Union, overload

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object

_SERIALIZER = Serializer()

# fmt: off

def build_get_valid_request(
    **kwargs: Any
) -> HttpRequest:
    """Get complex types that have readonly properties.

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
    _url = "/complex/readonlyproperty/valid"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_put_valid_request(
    *,
    json: JSON,
    content_type: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Put complex types that have readonly properties.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Required.
    :paramtype json: JSON
    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional.
                "size": 0  # Optional.
            }
    """

    ...

@overload
def build_put_valid_request(
    *,
    content: IO,
    content_type: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Put complex types that have readonly properties.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content: Required.
    :paramtype content: IO
    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    ...

def build_put_valid_request(
    **kwargs: Any
) -> HttpRequest:
    """Put complex types that have readonly properties.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Is either a model type or a IO type. Required.
    :paramtype json: JSON or IO
    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/complex/readonlyproperty/valid"

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
