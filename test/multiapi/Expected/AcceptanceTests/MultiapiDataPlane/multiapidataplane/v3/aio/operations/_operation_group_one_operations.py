# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._operation_group_one_operations import build_test_two_request

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class OperationGroupOneOperations:
    """OperationGroupOneOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~multiapidataplane.v3.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def test_two(
        self,
        parameter_one: Optional["_models.ModelThree"] = None,
        **kwargs: Any
    ) -> "_models.ModelThree":
        """TestTwo should be in OperationGroupOneOperations. Takes in ModelThree and ouputs ModelThree.

        :param parameter_one: A ModelThree parameter.
        :type parameter_one: ~multiapidataplane.v3.models.ModelThree
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ModelThree, or the result of cls(response)
        :rtype: ~multiapidataplane.v3.models.ModelThree
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ModelThree"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if parameter_one is not None:
            json = self._serialize.body(parameter_one, 'ModelThree')
        else:
            json = None

        request = build_test_two_request(
            content_type=content_type,
            json=json,
            template_url=self.test_two.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ModelThree', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    test_two.metadata = {'url': '/multiapi/one/testTwoEndpoint'}  # type: ignore

