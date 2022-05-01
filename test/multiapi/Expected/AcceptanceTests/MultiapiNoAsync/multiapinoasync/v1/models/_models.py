# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError

from ... import _serialization


class Error(_serialization.Model):
    """Error.

    :ivar status:
    :vartype status: int
    :ivar message:
    :vartype message: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super(Error, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.message = kwargs.get('message', None)


class PagingResult(_serialization.Model):
    """PagingResult.

    :ivar values:
    :vartype values: list[~multiapinoasync.v1.models.Product]
    :ivar next_link:
    :vartype next_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[Product]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword values:
        :paramtype values: list[~multiapinoasync.v1.models.Product]
        :keyword next_link:
        :paramtype next_link: str
        """
        super(PagingResult, self).__init__(**kwargs)
        self.values = kwargs.get('values', None)
        self.next_link = kwargs.get('next_link', None)


class Product(_serialization.Model):
    """Product.

    :ivar id:
    :vartype id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword id:
        :paramtype id: int
        """
        super(Product, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class TestLroAndPagingOptions(_serialization.Model):
    """Parameter group.

    :ivar maxresults: Sets the maximum number of items to return in the response.
    :vartype maxresults: int
    :ivar timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :vartype timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': 'maxresults', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword maxresults: Sets the maximum number of items to return in the response.
        :paramtype maxresults: int
        :keyword timeout: Sets the maximum time that the server can spend processing the request, in
         seconds. The default is 30 seconds.
        :paramtype timeout: int
        """
        super(TestLroAndPagingOptions, self).__init__(**kwargs)
        self.maxresults = kwargs.get('maxresults', None)
        self.timeout = kwargs.get('timeout', 30)
