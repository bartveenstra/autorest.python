# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .. import models
from .._serialization import Deserializer, Serializer
from ._configuration import AutoRestParameterizedCustomHostTestClientConfiguration
from .operations import PathsOperations


class AutoRestParameterizedCustomHostTestClient:
    """Test Infrastructure for AutoRest.

    :ivar paths: PathsOperations operations
    :vartype paths: custombaseurlmoreoptions.aio.operations.PathsOperations
    :param subscription_id: The subscription id with value 'test12'. Required.
    :type subscription_id: str
    :param dns_suffix: A string value that is used as a global part of the parameterized host.
     Default value 'host'. Default value is "host".
    :type dns_suffix: str
    """

    def __init__(self, subscription_id: str, dns_suffix: str = "host", **kwargs: Any) -> None:
        _endpoint = "{vault}{secret}{dnsSuffix}"
        self._config = AutoRestParameterizedCustomHostTestClientConfiguration(
            subscription_id=subscription_id, dns_suffix=dns_suffix, **kwargs
        )
        self._client = AsyncPipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.paths = PathsOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "dnsSuffix": self._serialize.url(
                "self._config.dns_suffix", self._config.dns_suffix, "str", skip_quote=True
            ),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestParameterizedCustomHostTestClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
