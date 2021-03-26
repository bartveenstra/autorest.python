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
    from typing import Any, IO, Optional, Union

_SERIALIZER = Serializer()


def prepare_test_paging(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Returns ModelThree with optionalProperty 'paged'.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/paging')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    return HttpRequest(
        method="GET",
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
    :param greeting_in_chinese: pass in 'nihao' to pass test.
    :type greeting_in_chinese: str
    :param greeting_in_french: pass in 'bonjour' to pass test.
    :type greeting_in_french: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    greeting_in_english = kwargs.pop('greeting_in_english')  # type: str
    greeting_in_chinese = kwargs.pop('greeting_in_chinese', None)  # type: Optional[str]
    greeting_in_french = kwargs.pop('greeting_in_french', None)  # type: Optional[str]
    api_version = "3.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testDifferentCalls')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['greetingInEnglish'] = _SERIALIZER.header("greeting_in_english", greeting_in_english, 'str')
    if greeting_in_chinese is not None:
        header_parameters['greetingInChinese'] = _SERIALIZER.header("greeting_in_chinese", greeting_in_chinese, 'str')
    if greeting_in_french is not None:
        header_parameters['greetingInFrench'] = _SERIALIZER.header("greeting_in_french", greeting_in_french, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_operationgroupone_test_two(
    parameter_one=None,  # type: Optional["_models.ModelThree"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """TestTwo should be in OperationGroupOneOperations. Takes in ModelThree and ouputs ModelThree.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param parameter_one: A ModelThree parameter.
    :type parameter_one: ~multiapidataplane.v3.models.ModelThree
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "3.0.0"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/one/testTwoEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs['json'] = parameter_one

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **body_content_kwargs
    )


def prepare_operationgrouptwo_test_four(
    input=None,  # type: Optional[Union[IO, "_models.SourcePath"]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """TestFour should be in OperationGroupTwoOperations.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param input: Input parameter.
    :type input: IO or ~multiapidataplane.v3.models.SourcePath
    :keyword str content_type: Media type of the body sent to the API. Default value is "application/json".
     Allowed values are: "application/pdf", "image/jpeg", "image/png", "image/tiff", "application/json".
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "3.0.0"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/two/testFourEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    if header_parameters['Content-Type'].split(";")[0] in ['application/pdf', 'image/jpeg', 'image/png', 'image/tiff']:
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs['content'] = input

    elif header_parameters['Content-Type'].split(";")[0] in ['application/json']:
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs['json'] = input
    else:
        raise ValueError(
            "The content_type '{}' is not one of the allowed values: "
            "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(header_parameters['Content-Type'])
        )

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **body_content_kwargs
    )


def prepare_operationgrouptwo_test_five(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """TestFive should be in OperationGroupTwoOperations.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    api_version = "3.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/two/testFiveEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
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
