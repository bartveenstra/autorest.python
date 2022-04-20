# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..._serialization import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

_SERIALIZER = Serializer()

# fmt: off

def build_get_with_filter_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Specify filter parameter with value '$filter=id gt 5 and name eq 'foo'&$orderby=id&$top=10'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword filter: The filter parameter with value '$filter=id gt 5 and name eq 'foo''. Default
     value is None.
    :paramtype filter: str
    :keyword top: The top parameter with value 10. Default value is None.
    :paramtype top: int
    :keyword orderby: The orderby parameter with value id. Default value is None.
    :paramtype orderby: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    filter = kwargs.pop('filter', _params.pop('$filter', None))  # type: Optional[str]
    top = kwargs.pop('top', _params.pop('$top', None))  # type: Optional[int]
    orderby = kwargs.pop('orderby', _params.pop('$orderby', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/azurespecials/odata/filter"

    # Construct parameters
    if filter is not None:
        _params['$filter'] = _SERIALIZER.query("filter", filter, 'str')
    if top is not None:
        _params['$top'] = _SERIALIZER.query("top", top, 'int')
    if orderby is not None:
        _params['$orderby'] = _SERIALIZER.query("orderby", orderby, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )
