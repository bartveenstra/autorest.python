# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.paths_operations import PathsOperations
from .operations.queries_operations import QueriesOperations
from .operations.path_items_operations import PathItemsOperations
from . import models


class AutoRestUrlTestServiceConfiguration(Configuration):
    """Configuration for AutoRestUrlTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param global_string_path: A string value 'globalItemStringPath' that
     appears in the path
    :type global_string_path: str
    :param global_string_query: should contain value null
    :type global_string_query: str
    :param str base_url: Service URL
    """

    def __init__(
            self, global_string_path, global_string_query=None, base_url=None):

        if global_string_path is None:
            raise ValueError("Parameter 'global_string_path' must not be None.")
        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestUrlTestServiceConfiguration, self).__init__(base_url)

        self.add_user_agent('autoresturltestservice/{}'.format(VERSION))

        self.global_string_path = global_string_path
        self.global_string_query = global_string_query


class AutoRestUrlTestService(SDKClient):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestUrlTestServiceConfiguration

    :ivar paths: Paths operations
    :vartype paths: url.operations.PathsOperations
    :ivar queries: Queries operations
    :vartype queries: url.operations.QueriesOperations
    :ivar path_items: PathItems operations
    :vartype path_items: url.operations.PathItemsOperations

    :param global_string_path: A string value 'globalItemStringPath' that
     appears in the path
    :type global_string_path: str
    :param global_string_query: should contain value null
    :type global_string_query: str
    :param str base_url: Service URL
    """

    def __init__(
            self, global_string_path, global_string_query=None, base_url=None):

        self.config = AutoRestUrlTestServiceConfiguration(global_string_path, global_string_query, base_url)
        super(AutoRestUrlTestService, self).__init__(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paths = PathsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.queries = QueriesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.path_items = PathItemsOperations(
            self._client, self.config, self._serialize, self._deserialize)