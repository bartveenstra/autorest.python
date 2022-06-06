# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from .. import _serialization


class AvailabilitySetUpdateParameters(_serialization.Model):
    """AvailabilitySetUpdateParameters.

    All required parameters must be populated in order to send to Azure.

    :ivar tags: A description about the set of tags. Required.
    :vartype tags: dict[str, str]
    """

    _validation = {
        "tags": {"required": True},
    }

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, **kwargs):
        """
        :keyword tags: A description about the set of tags. Required.
        :paramtype tags: dict[str, str]
        """
        super(AvailabilitySetUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs["tags"]
