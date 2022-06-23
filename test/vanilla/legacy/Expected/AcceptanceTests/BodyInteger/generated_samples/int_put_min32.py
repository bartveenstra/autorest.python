# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from bodyinteger import AutoRestIntegerTestService

"""
# PREREQUISITES
    pip install autorestintegertestservice
# USAGE
    python int_put_min32.py
"""


def main():
    client = AutoRestIntegerTestService()

    response = client.int.put_min32(
        int_body=-2147483648,
    )
    print(response)


if __name__ == "__main__":
    main()
