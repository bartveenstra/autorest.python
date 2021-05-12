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
    from typing import Any, Optional

_SERIALIZER = Serializer()


def prepare_test_one(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """TestOne should be in an FirstVersionOperationsMixin.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param id: An int parameter.
    :type id: int
    :param message: An optional string parameter.
    :type message: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    id = kwargs.pop('id')  # type: int
    message = kwargs.pop('message', None)  # type: Optional[str]
    api_version = "1.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testOneEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['id'] = _SERIALIZER.query("id", id, 'int')
    if message is not None:
        query_parameters['message'] = _SERIALIZER.query("message", message, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_test_lro_initial(
    product=None,  # type: Optional["_models.Product"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put in whatever shape of Product you want, will return a Product with id equal to 100.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param product: Product to put.
    :type product: ~multiapi.v1.models.Product
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/lro')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs['json'] = product

    return HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **body_content_kwargs
    )


def prepare_test_lro_and_paging_initial(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A long-running paging operation that includes a nextLink that has 10 pages.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param client_request_id:
    :type client_request_id: str
    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :type timeout: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    client_request_id = kwargs.pop('client_request_id', None)  # type: Optional[str]
    maxresults = kwargs.pop('maxresults', None)  # type: Optional[int]
    timeout = kwargs.pop('timeout', 30)  # type: Optional[int]
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/lroAndPaging')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters['client-request-id'] = _SERIALIZER.header("client_request_id", client_request_id, 'str')
    if maxresults is not None:
        header_parameters['maxresults'] = _SERIALIZER.header("maxresults", maxresults, 'int')
    if timeout is not None:
        header_parameters['timeout'] = _SERIALIZER.header("timeout", timeout, 'int')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )


def prepare_test_different_calls(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Has added parameters across the API versions.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param greeting_in_english: pass in 'hello' to pass test.
    :type greeting_in_english: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    greeting_in_english = kwargs.pop('greeting_in_english')  # type: str
    api_version = "1.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testDifferentCalls')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['greetingInEnglish'] = _SERIALIZER.header("greeting_in_english", greeting_in_english, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_operationgroupone_test_two(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """TestTwo should be in OperationGroupOneOperations.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "1.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/one/testTwoEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )
