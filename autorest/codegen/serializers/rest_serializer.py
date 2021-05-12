# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
from typing import List
from abc import abstractmethod
from jinja2 import Environment

from ..models import RequestBuilder
from .import_serializer import FileImportSerializer
from ..models import CodeModel

class RestSerializer:
    def __init__(
        self, code_model: CodeModel, env: Environment, request_builders: List[RequestBuilder]
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.request_builders = request_builders

    def serialize_init(self) -> str:
        template = self.env.get_template("rest_init.py.jinja2")
        return template.render(code_model=self.code_model, request_builders=self.request_builders)

def serialize_json_dict(template_representation):
    return json.dumps(template_representation, sort_keys=True, indent=4)

class RestPython3Serializer(RestSerializer):

    def serialize_request_builders(self) -> str:
        template = self.env.get_template("request_builders.py.jinja2")

        return template.render(
            code_model=self.code_model,
            request_builders=self.request_builders,
            imports=FileImportSerializer(
                self.code_model.rest.imports(self.code_model),
                is_python_3_file=True
            ),
            is_python_3_file=True,
            serialize_json_dict=serialize_json_dict,
        )

class RestGenericSerializer(RestSerializer):

    def serialize_request_builders(self) -> str:
        template = self.env.get_template("request_builders.py.jinja2")

        return template.render(
            code_model=self.code_model,
            request_builders=self.request_builders,
            imports=FileImportSerializer(
                self.code_model.rest.imports(self.code_model),
                is_python_3_file=False
            ),
            is_python_3_file=False,
            serialize_json_dict=serialize_json_dict,
        )