# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, IO, Optional, Union, overload

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

@overload
def build_put201_creating_succeeded200_request(
    *,
    content_type: Optional[str] = None,
    json: Optional[JSON] = None,
    **kwargs: Any
) -> HttpRequest:
    """Long running put request, service returns a 500, then a 201 to the initial request, with an
    entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
    returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", and "OK".
                },
                "tags": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """


@overload
def build_put201_creating_succeeded200_request(
    *,
    content_type: Optional[str] = None,
    content: Optional[IO] = None,
    **kwargs: Any
) -> HttpRequest:
    """Long running put request, service returns a 500, then a 201 to the initial request, with an
    entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
    returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Product to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_put201_creating_succeeded200_request(
    **kwargs: Any
) -> HttpRequest:
    """Long running put request, service returns a 500, then a 201 to the initial request, with an
    entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
    returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Is either a model type or a IO type. Default value is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/put/201/creating/succeeded/200"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_put_async_relative_retry_succeeded_request(
    *,
    content_type: Optional[str] = None,
    json: Optional[JSON] = None,
    **kwargs: Any
) -> HttpRequest:
    """Long running put request, service returns a 500, then a 200 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", and "OK".
                },
                "tags": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """


@overload
def build_put_async_relative_retry_succeeded_request(
    *,
    content_type: Optional[str] = None,
    content: Optional[IO] = None,
    **kwargs: Any
) -> HttpRequest:
    """Long running put request, service returns a 500, then a 200 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Product to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_put_async_relative_retry_succeeded_request(
    **kwargs: Any
) -> HttpRequest:
    """Long running put request, service returns a 500, then a 200 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Is either a model type or a IO type. Default value is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/putasync/retry/succeeded"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_delete_provisioning202_accepted200_succeeded_request(
    **kwargs: Any
) -> HttpRequest:
    """Long running delete request, service returns a 500, then a  202 to the initial request, with an
    entity that contains ProvisioningState=’Accepted’.  Polls return this value until the last poll
    returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/delete/provisioning/202/accepted/200/succeeded"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_delete202_retry200_request(
    **kwargs: Any
) -> HttpRequest:
    """Long running delete request, service returns a 500, then a 202 to the initial request. Polls
    return this value until the last poll returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/delete/202/retry/200"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_delete_async_relative_retry_succeeded_request(
    **kwargs: Any
) -> HttpRequest:
    """Long running delete request, service returns a 500, then a 202 to the initial request. Poll the
    endpoint indicated in the Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/deleteasync/retry/succeeded"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_post202_retry200_request(
    *,
    content_type: Optional[str] = None,
    json: Optional[JSON] = None,
    **kwargs: Any
) -> HttpRequest:
    """Long running post request, service returns a 500, then a 202 to the initial request, with
    'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", and "OK".
                },
                "tags": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """


@overload
def build_post202_retry200_request(
    *,
    content_type: Optional[str] = None,
    content: Optional[IO] = None,
    **kwargs: Any
) -> HttpRequest:
    """Long running post request, service returns a 500, then a 202 to the initial request, with
    'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Product to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_post202_retry200_request(
    **kwargs: Any
) -> HttpRequest:
    """Long running post request, service returns a 500, then a 202 to the initial request, with
    'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Is either a model type or a IO type. Default value is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/post/202/retry/200"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_post_async_relative_retry_succeeded_request(
    *,
    content_type: Optional[str] = None,
    json: Optional[JSON] = None,
    **kwargs: Any
) -> HttpRequest:
    """Long running post request, service returns a 500, then a 202 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", and "OK".
                },
                "tags": {
                    "str": "str"  # Optional. Dictionary of :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """


@overload
def build_post_async_relative_retry_succeeded_request(
    *,
    content_type: Optional[str] = None,
    content: Optional[IO] = None,
    **kwargs: Any
) -> HttpRequest:
    """Long running post request, service returns a 500, then a 202 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Product to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_post_async_relative_retry_succeeded_request(
    **kwargs: Any
) -> HttpRequest:
    """Long running post request, service returns a 500, then a 202 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Product to put. Is either a model type or a IO type. Default value is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/postasync/retry/succeeded"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )
