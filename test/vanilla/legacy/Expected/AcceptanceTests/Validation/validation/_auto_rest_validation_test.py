# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core import PipelineClient

from . import models
from ._configuration import AutoRestValidationTestConfiguration
from .operations import AutoRestValidationTestOperationsMixin

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.rest import HttpRequest, HttpResponse


class AutoRestValidationTest(
    AutoRestValidationTestOperationsMixin
):  # pylint: disable=client-accepts-api-version-keyword
    """Test Infrastructure for AutoRest. No server backend exists for these tests.

    :param subscription_id: Subscription ID. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "http://localhost:3000".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "1.0.0". Note that overriding this default
     value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        subscription_id,  # type: str
        base_url="http://localhost:3000",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        self._config = AutoRestValidationTestConfiguration(subscription_id=subscription_id, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    def _send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestValidationTest
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
