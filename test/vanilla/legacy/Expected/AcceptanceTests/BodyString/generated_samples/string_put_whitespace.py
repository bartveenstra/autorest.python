# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from bodystring import AutoRestSwaggerBATService

"""
# PREREQUISITES
    pip install autorestswaggerbatservice
# USAGE
    python string_put_whitespace.py
"""


def main():
    client = AutoRestSwaggerBATService()

    response = client.string.put_whitespace()
    print(response)


if __name__ == "__main__":
    main()
