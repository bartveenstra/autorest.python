# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from bodydatetime import AutoRestDateTimeTestService

"""
The sample just shows how to use the method and may not run successfully.
# PREREQUISITES
    pip install AutoRestDateTimeTestService
# USAGE
    python datetime_put_utc_min_date_time.py
"""


def main():
    client = AutoRestDateTimeTestService()

    response = client.datetime.put_utc_min_date_time(
        datetime_body="0001-01-01T00:00:00Z",
    )
    print(response)


if __name__ == "__main__":
    main()