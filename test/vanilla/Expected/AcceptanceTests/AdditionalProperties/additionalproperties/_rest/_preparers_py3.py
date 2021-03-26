# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any

from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def prepare_pets_create_ap_true(create_parameters: "_models.PetAPTrue", **kwargs: Any) -> HttpRequest:
    """Create a Pet which contains more properties than what is defined.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param create_parameters:
    :type create_parameters: ~additionalproperties.models.PetAPTrue
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/additionalProperties/true")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = create_parameters

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **body_content_kwargs)


def prepare_pets_create_cat_ap_true(create_parameters: "_models.CatAPTrue", **kwargs: Any) -> HttpRequest:
    """Create a CatAPTrue which contains more properties than what is defined.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param create_parameters:
    :type create_parameters: ~additionalproperties.models.CatAPTrue
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/additionalProperties/true-subclass")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = create_parameters

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **body_content_kwargs)


def prepare_pets_create_ap_object(create_parameters: "_models.PetAPObject", **kwargs: Any) -> HttpRequest:
    """Create a Pet which contains more properties than what is defined.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param create_parameters:
    :type create_parameters: ~additionalproperties.models.PetAPObject
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/additionalProperties/type/object")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = create_parameters

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **body_content_kwargs)


def prepare_pets_create_ap_string(create_parameters: "_models.PetAPString", **kwargs: Any) -> HttpRequest:
    """Create a Pet which contains more properties than what is defined.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param create_parameters:
    :type create_parameters: ~additionalproperties.models.PetAPString
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/additionalProperties/type/string")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = create_parameters

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **body_content_kwargs)


def prepare_pets_create_ap_in_properties(create_parameters: "_models.PetAPInProperties", **kwargs: Any) -> HttpRequest:
    """Create a Pet which contains more properties than what is defined.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param create_parameters:
    :type create_parameters: ~additionalproperties.models.PetAPInProperties
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/additionalProperties/in/properties")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = create_parameters

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **body_content_kwargs)


def prepare_pets_create_ap_in_properties_with_ap_string(
    create_parameters: "_models.PetAPInPropertiesWithAPString", **kwargs: Any
) -> HttpRequest:
    """Create a Pet which contains more properties than what is defined.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this preparer into your code flow.

    :param create_parameters:
    :type create_parameters: ~additionalproperties.models.PetAPInPropertiesWithAPString
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/additionalProperties/in/properties/with/additionalProperties/string")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["json"] = create_parameters

    return HttpRequest(method="PUT", url=url, headers=header_parameters, **body_content_kwargs)