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


class Pet(Model):
    """Pet.

    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Pet, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
