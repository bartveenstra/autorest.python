# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import prepare_datetime_get_null
    from ._preparers_py3 import prepare_datetime_get_invalid
    from ._preparers_py3 import prepare_datetime_get_overflow
    from ._preparers_py3 import prepare_datetime_get_underflow
    from ._preparers_py3 import prepare_datetime_put_utc_max_date_time
    from ._preparers_py3 import prepare_datetime_put_utc_max_date_time7_digits
    from ._preparers_py3 import prepare_datetime_get_utc_lowercase_max_date_time
    from ._preparers_py3 import prepare_datetime_get_utc_uppercase_max_date_time
    from ._preparers_py3 import prepare_datetime_get_utc_uppercase_max_date_time7_digits
    from ._preparers_py3 import prepare_datetime_put_local_positive_offset_max_date_time
    from ._preparers_py3 import prepare_datetime_get_local_positive_offset_lowercase_max_date_time
    from ._preparers_py3 import prepare_datetime_get_local_positive_offset_uppercase_max_date_time
    from ._preparers_py3 import prepare_datetime_put_local_negative_offset_max_date_time
    from ._preparers_py3 import prepare_datetime_get_local_negative_offset_uppercase_max_date_time
    from ._preparers_py3 import prepare_datetime_get_local_negative_offset_lowercase_max_date_time
    from ._preparers_py3 import prepare_datetime_put_utc_min_date_time
    from ._preparers_py3 import prepare_datetime_get_utc_min_date_time
    from ._preparers_py3 import prepare_datetime_put_local_positive_offset_min_date_time
    from ._preparers_py3 import prepare_datetime_get_local_positive_offset_min_date_time
    from ._preparers_py3 import prepare_datetime_put_local_negative_offset_min_date_time
    from ._preparers_py3 import prepare_datetime_get_local_negative_offset_min_date_time
    from ._preparers_py3 import prepare_datetime_get_local_no_offset_min_date_time
except (SyntaxError, ImportError):
    from ._preparers import prepare_datetime_get_null  # type: ignore
    from ._preparers import prepare_datetime_get_invalid  # type: ignore
    from ._preparers import prepare_datetime_get_overflow  # type: ignore
    from ._preparers import prepare_datetime_get_underflow  # type: ignore
    from ._preparers import prepare_datetime_put_utc_max_date_time  # type: ignore
    from ._preparers import prepare_datetime_put_utc_max_date_time7_digits  # type: ignore
    from ._preparers import prepare_datetime_get_utc_lowercase_max_date_time  # type: ignore
    from ._preparers import prepare_datetime_get_utc_uppercase_max_date_time  # type: ignore
    from ._preparers import prepare_datetime_get_utc_uppercase_max_date_time7_digits  # type: ignore
    from ._preparers import prepare_datetime_put_local_positive_offset_max_date_time  # type: ignore
    from ._preparers import prepare_datetime_get_local_positive_offset_lowercase_max_date_time  # type: ignore
    from ._preparers import prepare_datetime_get_local_positive_offset_uppercase_max_date_time  # type: ignore
    from ._preparers import prepare_datetime_put_local_negative_offset_max_date_time  # type: ignore
    from ._preparers import prepare_datetime_get_local_negative_offset_uppercase_max_date_time  # type: ignore
    from ._preparers import prepare_datetime_get_local_negative_offset_lowercase_max_date_time  # type: ignore
    from ._preparers import prepare_datetime_put_utc_min_date_time  # type: ignore
    from ._preparers import prepare_datetime_get_utc_min_date_time  # type: ignore
    from ._preparers import prepare_datetime_put_local_positive_offset_min_date_time  # type: ignore
    from ._preparers import prepare_datetime_get_local_positive_offset_min_date_time  # type: ignore
    from ._preparers import prepare_datetime_put_local_negative_offset_min_date_time  # type: ignore
    from ._preparers import prepare_datetime_get_local_negative_offset_min_date_time  # type: ignore
    from ._preparers import prepare_datetime_get_local_no_offset_min_date_time  # type: ignore

__all__ = [
    "prepare_datetime_get_null",
    "prepare_datetime_get_invalid",
    "prepare_datetime_get_overflow",
    "prepare_datetime_get_underflow",
    "prepare_datetime_put_utc_max_date_time",
    "prepare_datetime_put_utc_max_date_time7_digits",
    "prepare_datetime_get_utc_lowercase_max_date_time",
    "prepare_datetime_get_utc_uppercase_max_date_time",
    "prepare_datetime_get_utc_uppercase_max_date_time7_digits",
    "prepare_datetime_put_local_positive_offset_max_date_time",
    "prepare_datetime_get_local_positive_offset_lowercase_max_date_time",
    "prepare_datetime_get_local_positive_offset_uppercase_max_date_time",
    "prepare_datetime_put_local_negative_offset_max_date_time",
    "prepare_datetime_get_local_negative_offset_uppercase_max_date_time",
    "prepare_datetime_get_local_negative_offset_lowercase_max_date_time",
    "prepare_datetime_put_utc_min_date_time",
    "prepare_datetime_get_utc_min_date_time",
    "prepare_datetime_put_local_positive_offset_min_date_time",
    "prepare_datetime_get_local_positive_offset_min_date_time",
    "prepare_datetime_put_local_negative_offset_min_date_time",
    "prepare_datetime_get_local_negative_offset_min_date_time",
    "prepare_datetime_get_local_no_offset_min_date_time",
]