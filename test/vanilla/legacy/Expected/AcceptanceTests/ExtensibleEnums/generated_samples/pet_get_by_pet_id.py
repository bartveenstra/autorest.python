# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from extensibleenumsswagger import PetStoreInc

"""
The sample just shows how to use the method and may not run successfully.
# PREREQUISITES
    pip install petstoreinc
# USAGE
    python pet_get_by_pet_id.py
"""


def main():
    client = PetStoreInc()

    response = client.pet.get_by_pet_id(
        pet_id="tommy",
    )
    print(response)


if __name__ == "__main__":
    main()
