# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import prepare_string_get_null
    from ._preparers_py3 import prepare_string_put_null
    from ._preparers_py3 import prepare_string_get_empty
    from ._preparers_py3 import prepare_string_put_empty
    from ._preparers_py3 import prepare_string_get_mbcs
    from ._preparers_py3 import prepare_string_put_mbcs
    from ._preparers_py3 import prepare_string_get_whitespace
    from ._preparers_py3 import prepare_string_put_whitespace
    from ._preparers_py3 import prepare_string_get_not_provided
    from ._preparers_py3 import prepare_string_get_base64_encoded
    from ._preparers_py3 import prepare_string_get_base64_url_encoded
    from ._preparers_py3 import prepare_string_put_base64_url_encoded
    from ._preparers_py3 import prepare_string_get_null_base64_url_encoded
    from ._preparers_py3 import prepare_enum_get_not_expandable
    from ._preparers_py3 import prepare_enum_put_not_expandable
    from ._preparers_py3 import prepare_enum_get_referenced
    from ._preparers_py3 import prepare_enum_put_referenced
    from ._preparers_py3 import prepare_enum_get_referenced_constant
    from ._preparers_py3 import prepare_enum_put_referenced_constant
except (SyntaxError, ImportError):
    from ._preparers import prepare_string_get_null  # type: ignore
    from ._preparers import prepare_string_put_null  # type: ignore
    from ._preparers import prepare_string_get_empty  # type: ignore
    from ._preparers import prepare_string_put_empty  # type: ignore
    from ._preparers import prepare_string_get_mbcs  # type: ignore
    from ._preparers import prepare_string_put_mbcs  # type: ignore
    from ._preparers import prepare_string_get_whitespace  # type: ignore
    from ._preparers import prepare_string_put_whitespace  # type: ignore
    from ._preparers import prepare_string_get_not_provided  # type: ignore
    from ._preparers import prepare_string_get_base64_encoded  # type: ignore
    from ._preparers import prepare_string_get_base64_url_encoded  # type: ignore
    from ._preparers import prepare_string_put_base64_url_encoded  # type: ignore
    from ._preparers import prepare_string_get_null_base64_url_encoded  # type: ignore
    from ._preparers import prepare_enum_get_not_expandable  # type: ignore
    from ._preparers import prepare_enum_put_not_expandable  # type: ignore
    from ._preparers import prepare_enum_get_referenced  # type: ignore
    from ._preparers import prepare_enum_put_referenced  # type: ignore
    from ._preparers import prepare_enum_get_referenced_constant  # type: ignore
    from ._preparers import prepare_enum_put_referenced_constant  # type: ignore

__all__ = [
    "prepare_string_get_null",
    "prepare_string_put_null",
    "prepare_string_get_empty",
    "prepare_string_put_empty",
    "prepare_string_get_mbcs",
    "prepare_string_put_mbcs",
    "prepare_string_get_whitespace",
    "prepare_string_put_whitespace",
    "prepare_string_get_not_provided",
    "prepare_string_get_base64_encoded",
    "prepare_string_get_base64_url_encoded",
    "prepare_string_put_base64_url_encoded",
    "prepare_string_get_null_base64_url_encoded",
    "prepare_enum_get_not_expandable",
    "prepare_enum_put_not_expandable",
    "prepare_enum_get_referenced",
    "prepare_enum_put_referenced",
    "prepare_enum_get_referenced_constant",
    "prepare_enum_put_referenced_constant",
]