# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from .. import _serialization


class SourcePath(_serialization.Model):
    """Uri or local path to source data.

    :ivar source: File source path.
    :vartype source: str
    """

    _validation = {
        "source": {"max_length": 2048},
    }

    _attribute_map = {
        "source": {"key": "source", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword source: File source path.
        :paramtype source: str
        """
        super(SourcePath, self).__init__(**kwargs)
        self.source = kwargs.get("source", None)
