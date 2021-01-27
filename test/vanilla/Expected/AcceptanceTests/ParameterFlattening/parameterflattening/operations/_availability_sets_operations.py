# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class AvailabilitySetsOperations(object):
    """AvailabilitySetsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~parameterflattening.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _update_request(
        self,
        resource_group_name,  # type: str
        avset,  # type: str
        tags,  # type: Dict[str, str]
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpRequest

        body = _models.AvailabilitySetUpdateParameters(tags=tags)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._update_request.metadata["url"]  # type: ignore
        path_format_arguments = {
            "resourceGroupName": self._serialize.url("resource_group_name", resource_group_name, "str"),
            "availabilitySetName": self._serialize.url("avset", avset, "str", max_length=80, min_length=0),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "AvailabilitySetUpdateParameters")
        body_content_kwargs["content"] = body_content
        return self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

    _update_request.metadata = {"url": "/parameterFlattening/{resourceGroupName}/{availabilitySetName}"}  # type: ignore

    @distributed_trace
    def update(
        self,
        resource_group_name,  # type: str
        avset,  # type: str
        tags,  # type: Dict[str, str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Updates the tags for an availability set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param avset: The name of the storage availability set.
        :type avset: str
        :param tags: A description about the set of tags.
        :type tags: dict[str, str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = self._update_request(resource_group_name=resource_group_name, avset=avset, tags=tags, **kwargs)
        kwargs.pop("content_type", None)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    update.metadata = {"url": "/parameterFlattening/{resourceGroupName}/{availabilitySetName}"}  # type: ignore
