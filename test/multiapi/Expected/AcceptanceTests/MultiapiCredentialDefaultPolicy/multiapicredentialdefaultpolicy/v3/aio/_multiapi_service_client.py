# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core.credentials import AzureKeyCredential
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import MultiapiServiceClientConfiguration
from .operations import MultiapiServiceClientOperationsMixin
from .operations import OperationGroupOneOperations
from .operations import OperationGroupTwoOperations
from .. import models


class MultiapiServiceClient(MultiapiServiceClientOperationsMixin):
    """Service client for multiapi client testing.

    :ivar operation_group_one: OperationGroupOneOperations operations
    :vartype operation_group_one: multiapicredentialdefaultpolicy.v3.aio.operations.OperationGroupOneOperations
    :ivar operation_group_two: OperationGroupTwoOperations operations
    :vartype operation_group_two: multiapicredentialdefaultpolicy.v3.aio.operations.OperationGroupTwoOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.AzureKeyCredential
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: AzureKeyCredential,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = MultiapiServiceClientConfiguration(credential, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operation_group_one = OperationGroupOneOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_group_two = OperationGroupTwoOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        http_request.url = self._client.format_url(http_request.url)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MultiapiServiceClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
