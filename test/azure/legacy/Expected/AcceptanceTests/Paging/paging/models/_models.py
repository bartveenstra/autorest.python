# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class CustomParameterGroup(msrest.serialization.Model):
    """Parameter group.

    All required parameters must be populated in order to send to Azure.

    :ivar api_version: Required. Sets the api version to use.
    :vartype api_version: str
    :ivar tenant: Required. Sets the tenant to use.
    :vartype tenant: str
    """

    _validation = {
        "api_version": {"required": True},
        "tenant": {"required": True},
    }

    _attribute_map = {
        "api_version": {"key": "api_version", "type": "str"},
        "tenant": {"key": "tenant", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword api_version: Required. Sets the api version to use.
        :paramtype api_version: str
        :keyword tenant: Required. Sets the tenant to use.
        :paramtype tenant: str
        """
        super(CustomParameterGroup, self).__init__(**kwargs)
        self.api_version = kwargs["api_version"]
        self.tenant = kwargs["tenant"]


class OdataProductResult(msrest.serialization.Model):
    """OdataProductResult.

    :ivar values:
    :vartype values: list[~paging.models.Product]
    :ivar odata_next_link:
    :vartype odata_next_link: str
    """

    _attribute_map = {
        "values": {"key": "values", "type": "[Product]"},
        "odata_next_link": {"key": "odata\\.nextLink", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword values:
        :paramtype values: list[~paging.models.Product]
        :keyword odata_next_link:
        :paramtype odata_next_link: str
        """
        super(OdataProductResult, self).__init__(**kwargs)
        self.values = kwargs.get("values", None)
        self.odata_next_link = kwargs.get("odata_next_link", None)


class OperationResult(msrest.serialization.Model):
    """OperationResult.

    :ivar status: The status of the request. Known values are: "Succeeded", "Failed", "canceled",
     "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
    :vartype status: str or ~paging.models.OperationResultStatus
    """

    _attribute_map = {
        "status": {"key": "status", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword status: The status of the request. Known values are: "Succeeded", "Failed",
         "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted",
         "OK".
        :paramtype status: str or ~paging.models.OperationResultStatus
        """
        super(OperationResult, self).__init__(**kwargs)
        self.status = kwargs.get("status", None)


class PagingGetMultiplePagesLroOptions(msrest.serialization.Model):
    """Parameter group.

    :ivar maxresults: Sets the maximum number of items to return in the response.
    :vartype maxresults: int
    :ivar timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :vartype timeout: int
    """

    _attribute_map = {
        "maxresults": {"key": "maxresults", "type": "int"},
        "timeout": {"key": "timeout", "type": "int"},
    }

    def __init__(self, **kwargs):
        """
        :keyword maxresults: Sets the maximum number of items to return in the response.
        :paramtype maxresults: int
        :keyword timeout: Sets the maximum time that the server can spend processing the request, in
         seconds. The default is 30 seconds.
        :paramtype timeout: int
        """
        super(PagingGetMultiplePagesLroOptions, self).__init__(**kwargs)
        self.maxresults = kwargs.get("maxresults", None)
        self.timeout = kwargs.get("timeout", 30)


class PagingGetMultiplePagesOptions(msrest.serialization.Model):
    """Parameter group.

    :ivar maxresults: Sets the maximum number of items to return in the response.
    :vartype maxresults: int
    :ivar timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :vartype timeout: int
    """

    _attribute_map = {
        "maxresults": {"key": "maxresults", "type": "int"},
        "timeout": {"key": "timeout", "type": "int"},
    }

    def __init__(self, **kwargs):
        """
        :keyword maxresults: Sets the maximum number of items to return in the response.
        :paramtype maxresults: int
        :keyword timeout: Sets the maximum time that the server can spend processing the request, in
         seconds. The default is 30 seconds.
        :paramtype timeout: int
        """
        super(PagingGetMultiplePagesOptions, self).__init__(**kwargs)
        self.maxresults = kwargs.get("maxresults", None)
        self.timeout = kwargs.get("timeout", 30)


class PagingGetMultiplePagesWithOffsetOptions(msrest.serialization.Model):
    """Parameter group.

    All required parameters must be populated in order to send to Azure.

    :ivar maxresults: Sets the maximum number of items to return in the response.
    :vartype maxresults: int
    :ivar offset: Required. Offset of return value.
    :vartype offset: int
    :ivar timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :vartype timeout: int
    """

    _validation = {
        "offset": {"required": True},
    }

    _attribute_map = {
        "maxresults": {"key": "maxresults", "type": "int"},
        "offset": {"key": "offset", "type": "int"},
        "timeout": {"key": "timeout", "type": "int"},
    }

    def __init__(self, **kwargs):
        """
        :keyword maxresults: Sets the maximum number of items to return in the response.
        :paramtype maxresults: int
        :keyword offset: Required. Offset of return value.
        :paramtype offset: int
        :keyword timeout: Sets the maximum time that the server can spend processing the request, in
         seconds. The default is 30 seconds.
        :paramtype timeout: int
        """
        super(PagingGetMultiplePagesWithOffsetOptions, self).__init__(**kwargs)
        self.maxresults = kwargs.get("maxresults", None)
        self.offset = kwargs["offset"]
        self.timeout = kwargs.get("timeout", 30)


class PagingGetOdataMultiplePagesOptions(msrest.serialization.Model):
    """Parameter group.

    :ivar maxresults: Sets the maximum number of items to return in the response.
    :vartype maxresults: int
    :ivar timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :vartype timeout: int
    """

    _attribute_map = {
        "maxresults": {"key": "maxresults", "type": "int"},
        "timeout": {"key": "timeout", "type": "int"},
    }

    def __init__(self, **kwargs):
        """
        :keyword maxresults: Sets the maximum number of items to return in the response.
        :paramtype maxresults: int
        :keyword timeout: Sets the maximum time that the server can spend processing the request, in
         seconds. The default is 30 seconds.
        :paramtype timeout: int
        """
        super(PagingGetOdataMultiplePagesOptions, self).__init__(**kwargs)
        self.maxresults = kwargs.get("maxresults", None)
        self.timeout = kwargs.get("timeout", 30)


class Product(msrest.serialization.Model):
    """Product.

    :ivar properties:
    :vartype properties: ~paging.models.ProductProperties
    """

    _attribute_map = {
        "properties": {"key": "properties", "type": "ProductProperties"},
    }

    def __init__(self, **kwargs):
        """
        :keyword properties:
        :paramtype properties: ~paging.models.ProductProperties
        """
        super(Product, self).__init__(**kwargs)
        self.properties = kwargs.get("properties", None)


class ProductProperties(msrest.serialization.Model):
    """ProductProperties.

    :ivar id:
    :vartype id: int
    :ivar name:
    :vartype name: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword id:
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        """
        super(ProductProperties, self).__init__(**kwargs)
        self.id = kwargs.get("id", None)
        self.name = kwargs.get("name", None)


class ProductResult(msrest.serialization.Model):
    """ProductResult.

    :ivar values:
    :vartype values: list[~paging.models.Product]
    :ivar next_link:
    :vartype next_link: str
    """

    _attribute_map = {
        "values": {"key": "values", "type": "[Product]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword values:
        :paramtype values: list[~paging.models.Product]
        :keyword next_link:
        :paramtype next_link: str
        """
        super(ProductResult, self).__init__(**kwargs)
        self.values = kwargs.get("values", None)
        self.next_link = kwargs.get("next_link", None)


class ProductResultValue(msrest.serialization.Model):
    """ProductResultValue.

    :ivar value:
    :vartype value: list[~paging.models.Product]
    :ivar next_link:
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[Product]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword value:
        :paramtype value: list[~paging.models.Product]
        :keyword next_link:
        :paramtype next_link: str
        """
        super(ProductResultValue, self).__init__(**kwargs)
        self.value = kwargs.get("value", None)
        self.next_link = kwargs.get("next_link", None)


class ProductResultValueWithXMSClientName(msrest.serialization.Model):
    """ProductResultValueWithXMSClientName.

    :ivar indexes:
    :vartype indexes: list[~paging.models.Product]
    :ivar next_link:
    :vartype next_link: str
    """

    _attribute_map = {
        "indexes": {"key": "values", "type": "[Product]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword indexes:
        :paramtype indexes: list[~paging.models.Product]
        :keyword next_link:
        :paramtype next_link: str
        """
        super(ProductResultValueWithXMSClientName, self).__init__(**kwargs)
        self.indexes = kwargs.get("indexes", None)
        self.next_link = kwargs.get("next_link", None)
