# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .error_py3 import Error, ErrorException
except (SyntaxError, ImportError):
    from .error import Error, ErrorException
from .auto_rest_url_test_service_enums import (
    UriColor,
)

__all__ = [
    'Error', 'ErrorException',
    'UriColor',
]
