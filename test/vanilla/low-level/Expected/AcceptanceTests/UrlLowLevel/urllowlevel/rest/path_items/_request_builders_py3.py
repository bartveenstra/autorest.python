# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Optional

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..._serialization import Serializer
from ..._vendor import _format_url_section

_SERIALIZER = Serializer()


def build_get_all_with_values_request(
    path_item_string_path: str,
    global_string_path: str,
    local_string_path: str,
    *,
    path_item_string_query: Optional[str] = None,
    global_string_query: Optional[str] = None,
    local_string_query: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
    localStringPath='localStringPath', globalStringQuery='globalStringQuery',
    pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
    :type path_item_string_path: str
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param local_string_path: should contain value 'localStringPath'.
    :type local_string_path: str
    :keyword path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
     parameter. Default value is None.
    :paramtype path_item_string_query: str
    :keyword global_string_query: should contain value null. Default value is None.
    :paramtype global_string_query: str
    :keyword local_string_query: should contain value 'localStringQuery'. Default value is None.
    :paramtype local_string_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/pathItemStringQuery/localStringQuery"  # pylint: disable=line-too-long
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, "str"),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, "str"),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if path_item_string_query is not None:
        _params["pathItemStringQuery"] = _SERIALIZER.query("path_item_string_query", path_item_string_query, "str")
    if global_string_query is not None:
        _params["globalStringQuery"] = _SERIALIZER.query("global_string_query", global_string_query, "str")
    if local_string_query is not None:
        _params["localStringQuery"] = _SERIALIZER.query("local_string_query", local_string_query, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_global_query_null_request(
    path_item_string_path: str,
    global_string_path: str,
    local_string_path: str,
    *,
    path_item_string_query: Optional[str] = None,
    global_string_query: Optional[str] = None,
    local_string_query: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
    localStringPath='localStringPath', globalStringQuery=null,
    pathItemStringQuery='pathItemStringQuery', localStringQuery='localStringQuery'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
    :type path_item_string_path: str
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param local_string_path: should contain value 'localStringPath'.
    :type local_string_path: str
    :keyword path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
     parameter. Default value is None.
    :paramtype path_item_string_query: str
    :keyword global_string_query: should contain value null. Default value is None.
    :paramtype global_string_query: str
    :keyword local_string_query: should contain value 'localStringQuery'. Default value is None.
    :paramtype local_string_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/localStringQuery"  # pylint: disable=line-too-long
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, "str"),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, "str"),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if path_item_string_query is not None:
        _params["pathItemStringQuery"] = _SERIALIZER.query("path_item_string_query", path_item_string_query, "str")
    if global_string_query is not None:
        _params["globalStringQuery"] = _SERIALIZER.query("global_string_query", global_string_query, "str")
    if local_string_query is not None:
        _params["localStringQuery"] = _SERIALIZER.query("local_string_query", local_string_query, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_global_and_local_query_null_request(
    path_item_string_path: str,
    global_string_path: str,
    local_string_path: str,
    *,
    path_item_string_query: Optional[str] = None,
    global_string_query: Optional[str] = None,
    local_string_query: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """send globalStringPath=globalStringPath, pathItemStringPath='pathItemStringPath',
    localStringPath='localStringPath', globalStringQuery=null,
    pathItemStringQuery='pathItemStringQuery', localStringQuery=null.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
    :type path_item_string_path: str
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param local_string_path: should contain value 'localStringPath'.
    :type local_string_path: str
    :keyword path_item_string_query: A string value 'pathItemStringQuery' that appears as a query
     parameter. Default value is None.
    :paramtype path_item_string_query: str
    :keyword global_string_query: should contain value null. Default value is None.
    :paramtype global_string_query: str
    :keyword local_string_query: should contain null value. Default value is None.
    :paramtype local_string_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/null/pathItemStringQuery/null"  # pylint: disable=line-too-long
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, "str"),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, "str"),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if path_item_string_query is not None:
        _params["pathItemStringQuery"] = _SERIALIZER.query("path_item_string_query", path_item_string_query, "str")
    if global_string_query is not None:
        _params["globalStringQuery"] = _SERIALIZER.query("global_string_query", global_string_query, "str")
    if local_string_query is not None:
        _params["localStringQuery"] = _SERIALIZER.query("local_string_query", local_string_query, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_local_path_item_query_null_request(
    path_item_string_path: str,
    global_string_path: str,
    local_string_path: str,
    *,
    path_item_string_query: Optional[str] = None,
    global_string_query: Optional[str] = None,
    local_string_query: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """send globalStringPath='globalStringPath', pathItemStringPath='pathItemStringPath',
    localStringPath='localStringPath', globalStringQuery='globalStringQuery',
    pathItemStringQuery=null, localStringQuery=null.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param path_item_string_path: A string value 'pathItemStringPath' that appears in the path.
    :type path_item_string_path: str
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param local_string_path: should contain value 'localStringPath'.
    :type local_string_path: str
    :keyword path_item_string_query: should contain value null. Default value is None.
    :paramtype path_item_string_query: str
    :keyword global_string_query: should contain value null. Default value is None.
    :paramtype global_string_query: str
    :keyword local_string_query: should contain value null. Default value is None.
    :paramtype local_string_query: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/pathitem/nullable/globalStringPath/{globalStringPath}/pathItemStringPath/{pathItemStringPath}/localStringPath/{localStringPath}/globalStringQuery/null/null"  # pylint: disable=line-too-long
    path_format_arguments = {
        "pathItemStringPath": _SERIALIZER.url("path_item_string_path", path_item_string_path, "str"),
        "globalStringPath": _SERIALIZER.url("global_string_path", global_string_path, "str"),
        "localStringPath": _SERIALIZER.url("local_string_path", local_string_path, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if path_item_string_query is not None:
        _params["pathItemStringQuery"] = _SERIALIZER.query("path_item_string_query", path_item_string_query, "str")
    if global_string_query is not None:
        _params["globalStringQuery"] = _SERIALIZER.query("global_string_query", global_string_query, "str")
    if local_string_query is not None:
        _params["localStringQuery"] = _SERIALIZER.query("local_string_query", local_string_query, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)
