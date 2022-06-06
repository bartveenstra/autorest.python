# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from .. import _serialization


class PathsJaneoqReservedwordsOperationDataPutRequestbodyContentApplicationXWwwFormUrlencodedSchema(
    _serialization.Model
):
    """PathsJaneoqReservedwordsOperationDataPutRequestbodyContentApplicationXWwwFormUrlencodedSchema.

    All required parameters must be populated in order to send to Azure.

    :ivar data: Pass in 'hello'. Required.
    :vartype data: str
    :ivar world: Pass in 'world'. Required.
    :vartype world: str
    """

    _validation = {
        "data": {"required": True},
        "world": {"required": True},
    }

    _attribute_map = {
        "data": {"key": "data", "type": "str"},
        "world": {"key": "world", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword data: Pass in 'hello'. Required.
        :paramtype data: str
        :keyword world: Pass in 'world'. Required.
        :paramtype world: str
        """
        super(
            PathsJaneoqReservedwordsOperationDataPutRequestbodyContentApplicationXWwwFormUrlencodedSchema, self
        ).__init__(**kwargs)
        self.data = kwargs["data"]
        self.world = kwargs["world"]


class PathsU1PxjnReservedwordsOperationFilesPutRequestbodyContentMultipartFormDataSchema(_serialization.Model):
    """PathsU1PxjnReservedwordsOperationFilesPutRequestbodyContentMultipartFormDataSchema.

    All required parameters must be populated in order to send to Azure.

    :ivar files: Files to upload. Pass in list of input streams. Required.
    :vartype files: IO
    :ivar file_name: File name to upload. Pass in 'my.txt'. Required.
    :vartype file_name: str
    """

    _validation = {
        "files": {"required": True},
        "file_name": {"required": True},
    }

    _attribute_map = {
        "files": {"key": "files", "type": "IO"},
        "file_name": {"key": "fileName", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword files: Files to upload. Pass in list of input streams. Required.
        :paramtype files: IO
        :keyword file_name: File name to upload. Pass in 'my.txt'. Required.
        :paramtype file_name: str
        """
        super(PathsU1PxjnReservedwordsOperationFilesPutRequestbodyContentMultipartFormDataSchema, self).__init__(
            **kwargs
        )
        self.files = kwargs["files"]
        self.file_name = kwargs["file_name"]
