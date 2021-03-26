# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, IO, List

_SERIALIZER = Serializer()


def prepare_formdata_upload_file(
    file_content,  # type: IO
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Upload file.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param file_content: File to upload.
    :type file_content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "multipart/form-data")
    accept = "application/octet-stream, application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/formdata/stream/uploadfile")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["files"] = file_content

    return HttpRequest(method="POST", url=url, headers=header_parameters, **body_content_kwargs)


def prepare_formdata_upload_file_via_body(
    file_content,  # type: IO
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Upload file.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param file_content: File to upload.
    :type file_content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "application/octet-stream")
    accept = "application/octet-stream, application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/formdata/stream/uploadfile")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["content"] = file_content

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **body_content_kwargs)


def prepare_formdata_upload_files(
    file_content,  # type: List[IO]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Upload multiple files.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param file_content: Files to upload.
    :type file_content: list[IO]
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "multipart/form-data")
    accept = "application/octet-stream, application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/formdata/stream/uploadfiles")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["files"] = file_content

    return HttpRequest(method="POST", url=url, headers=header_parameters, **body_content_kwargs)