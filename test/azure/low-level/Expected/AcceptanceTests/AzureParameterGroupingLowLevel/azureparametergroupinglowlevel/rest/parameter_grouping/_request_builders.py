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

from ..._vendor import _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

_SERIALIZER = Serializer()

# fmt: off

def build_post_required_request(
    path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Post a bunch of required parameters grouped.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param path: Path parameter.
    :type path: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input).
    :paramtype content: any
    :keyword custom_header:
    :paramtype custom_header: str
    :keyword query: Query parameter with default.
    :paramtype query: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = 0  # Optional.
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    custom_header = kwargs.pop('custom_header', None)  # type: Optional[str]
    query = kwargs.pop('query', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/parameterGrouping/postRequired/{path}')
    path_format_arguments = {
        "path": _SERIALIZER.url("path", path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if query is not None:
        query_parameters['query'] = _SERIALIZER.query("query", query, 'int')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if custom_header is not None:
        header_parameters['customHeader'] = _SERIALIZER.header("custom_header", custom_header, 'str')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_post_optional_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Post a bunch of optional parameters grouped.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword custom_header:
    :paramtype custom_header: str
    :keyword query: Query parameter with default.
    :paramtype query: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    custom_header = kwargs.pop('custom_header', None)  # type: Optional[str]
    query = kwargs.pop('query', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/parameterGrouping/postOptional')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if query is not None:
        query_parameters['query'] = _SERIALIZER.query("query", query, 'int')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if custom_header is not None:
        header_parameters['customHeader'] = _SERIALIZER.header("custom_header", custom_header, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_post_reserved_words_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Post a grouped parameters with reserved words.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword from_parameter: 'from' is a reserved word. Pass in 'bob' to pass.
    :paramtype from_parameter: str
    :keyword accept_parameter: 'accept' is a reserved word. Pass in 'yes' to pass.
    :paramtype accept_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    from_parameter = kwargs.pop('from_parameter', None)  # type: Optional[str]
    accept_parameter = kwargs.pop('accept_parameter', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/parameterGrouping/postReservedWords')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if from_parameter is not None:
        query_parameters['from'] = _SERIALIZER.query("from_parameter", from_parameter, 'str')
    if accept_parameter is not None:
        query_parameters['accept'] = _SERIALIZER.query("accept_parameter", accept_parameter, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_post_multi_param_groups_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Post parameters from multiple different parameter groups.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword header_one:
    :paramtype header_one: str
    :keyword query_one: Query parameter with default.
    :paramtype query_one: int
    :keyword header_two:
    :paramtype header_two: str
    :keyword query_two: Query parameter with default.
    :paramtype query_two: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    header_one = kwargs.pop('header_one', None)  # type: Optional[str]
    query_one = kwargs.pop('query_one', 30)  # type: Optional[int]
    header_two = kwargs.pop('header_two', None)  # type: Optional[str]
    query_two = kwargs.pop('query_two', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/parameterGrouping/postMultipleParameterGroups')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if query_one is not None:
        query_parameters['query-one'] = _SERIALIZER.query("query_one", query_one, 'int')
    if query_two is not None:
        query_parameters['query-two'] = _SERIALIZER.query("query_two", query_two, 'int')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if header_one is not None:
        header_parameters['header-one'] = _SERIALIZER.header("header_one", header_one, 'str')
    if header_two is not None:
        header_parameters['header-two'] = _SERIALIZER.header("header_two", header_two, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_post_shared_parameter_group_object_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Post parameters with a shared parameter group object.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword header_one:
    :paramtype header_one: str
    :keyword query_one: Query parameter with default.
    :paramtype query_one: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    header_one = kwargs.pop('header_one', None)  # type: Optional[str]
    query_one = kwargs.pop('query_one', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/parameterGrouping/sharedParameterGroupObject')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if query_one is not None:
        query_parameters['query-one'] = _SERIALIZER.query("query_one", query_one, 'int')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if header_one is not None:
        header_parameters['header-one'] = _SERIALIZER.header("header_one", header_one, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )
