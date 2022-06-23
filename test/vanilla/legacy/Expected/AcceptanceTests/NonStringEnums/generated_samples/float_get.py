# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from nonstringenums import NonStringEnumsClient

"""
# PREREQUISITES
    pip install nonstringenumsclient
# USAGE
    python float_get.py
"""


def main():
    client = NonStringEnumsClient()

    response = client.float.get()
    print(response)


if __name__ == "__main__":
    main()
