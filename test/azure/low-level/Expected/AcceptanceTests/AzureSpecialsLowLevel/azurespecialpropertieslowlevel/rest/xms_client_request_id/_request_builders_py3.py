# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..._serialization import Serializer

_SERIALIZER = Serializer()


def build_get_request(**kwargs: Any) -> HttpRequest:
    """Get method that overwrites x-ms-client-request header with value
    9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    _url = "/azurespecials/overwrite/x-ms-client-request-id/method/"

    return HttpRequest(method="GET", url=_url, **kwargs)


def build_param_get_request(*, x_ms_client_request_id: str, **kwargs: Any) -> HttpRequest:
    """Get method that overwrites x-ms-client-request header with value
    9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword x_ms_client_request_id: This should appear as a method parameter, use value
     '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'.
    :paramtype x_ms_client_request_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azurespecials/overwrite/x-ms-client-request-id/via-param/method/"

    # Construct headers
    _headers["x-ms-client-request-id"] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)
