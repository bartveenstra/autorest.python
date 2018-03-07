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

from msrest.serialization import Model


class ChildProduct(Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar const_property: Required. Constant string. Default value: "constant"
     .
    :vartype const_property: str
    :param count: Count
    :type count: int
    """

    _validation = {
        'const_property': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'const_property': {'key': 'constProperty', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
    }

    const_property = "constant"

    def __init__(self, *, count: int=None, **kwargs) -> None:
        super(ChildProduct, self).__init__(**kwargs)
        self.count = count
