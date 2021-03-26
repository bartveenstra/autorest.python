# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import prepare_files_get_file
    from ._preparers_py3 import prepare_files_get_file_large
    from ._preparers_py3 import prepare_files_get_empty_file
except (SyntaxError, ImportError):
    from ._preparers import prepare_files_get_file  # type: ignore
    from ._preparers import prepare_files_get_file_large  # type: ignore
    from ._preparers import prepare_files_get_empty_file  # type: ignore

__all__ = [
    "prepare_files_get_file",
    "prepare_files_get_file_large",
    "prepare_files_get_empty_file",
]