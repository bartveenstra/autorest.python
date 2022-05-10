# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Optional, cast
from jinja2 import Environment
from .import_serializer import FileImportSerializer, TypingSection
from ..models.imports import MsrestImportType
from ..models import (
    FileImport,
    ImportType,
    CodeModel,
    Parameter,
    TokenCredentialType,
    CredentialType,
)
from .client_serializer import ClientSerializer, ConfigSerializer


class GeneralSerializer:
    def __init__(
        self, code_model: CodeModel, env: Environment, async_mode: bool
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.async_mode = async_mode

    def serialize_pkgutil_init_file(self) -> str:
        template = self.env.get_template("pkgutil_init.py.jinja2")
        return template.render()

    def serialize_init_file(self) -> str:
        template = self.env.get_template("init.py.jinja2")
        return template.render(code_model=self.code_model, async_mode=self.async_mode)

    def _correct_credential_parameter(self, credential: Optional[Parameter]):
        if credential:
            credential.type = TokenCredentialType(
                credential.type.yaml_data,
                credential.type.code_model,
                async_mode=self.async_mode,
                policy=cast(CredentialType, credential.type).policy,
            )

    def serialize_service_client_file(self) -> str:

        template = self.env.get_template("client.py.jinja2")

        if self.code_model.credential and isinstance(
            self.code_model.credential.type, TokenCredentialType
        ):
            self._correct_credential_parameter(
                self.code_model.client.parameters.credential
            )

        python3_only = self.code_model.options["python3_only"]
        return template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
            serializer=ClientSerializer(self.code_model, is_python3_file=python3_only),
            imports=FileImportSerializer(
                self.code_model.client.imports(self.async_mode),
                is_python3_file=self.async_mode or python3_only,
            ),
        )

    def serialize_vendor_file(self) -> str:
        template = self.env.get_template("vendor.py.jinja2")

        # configure imports
        file_import = FileImport()
        if self.code_model.need_request_converter:
            file_import.add_submodule_import(
                "azure.core.pipeline.transport",
                "HttpRequest",
                ImportType.AZURECORE,
            )

        if self.code_model.need_mixin_abc:
            file_import.add_submodule_import(
                "abc",
                "ABC",
                ImportType.STDLIB,
            )
            file_import.add_submodule_import(
                "azure.core",
                f"{'Async' if self.async_mode else ''}PipelineClient",
                ImportType.AZURECORE,
                TypingSection.TYPING,
            )
            file_import.add_submodule_import(
                "._configuration",
                f"{self.code_model.client.name}Configuration",
                ImportType.LOCAL,
            )
            file_import.add_msrest_import(
                self.code_model,
                ".",
                MsrestImportType.SerializerDeserializer,
                TypingSection.TYPING,
            )

        return template.render(
            code_model=self.code_model,
            imports=FileImportSerializer(
                file_import,
                is_python3_file=self.async_mode,
            ),
            async_mode=self.async_mode,
        )

    def serialize_config_file(self) -> str:

        package_name = self.code_model.options["package_name"]
        if package_name and package_name.startswith("azure-"):
            package_name = package_name[len("azure-") :]
        sdk_moniker = (
            package_name if package_name else self.code_model.client.name.lower()
        )

        if self.code_model.credential and isinstance(
            self.code_model.credential.type, TokenCredentialType
        ):
            self._correct_credential_parameter(
                self.code_model.config.parameters.credential
            )

        template = self.env.get_template("config.py.jinja2")
        python3_only = self.code_model.options["python3_only"]
        return template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
            imports=FileImportSerializer(
                self.code_model.config.imports(self.async_mode),
                is_python3_file=self.async_mode or python3_only,
            ),
            serializer=ConfigSerializer(self.code_model, is_python3_file=python3_only),
            sdk_moniker=sdk_moniker,
        )

    def serialize_version_file(self) -> str:
        template = self.env.get_template("version.py.jinja2")
        return template.render(code_model=self.code_model)

    def serialize_setup_file(self) -> str:
        template = self.env.get_template("setup.py.jinja2")
        params = {}
        params.update(self.code_model.options)
        params.update(self.code_model.package_dependency)
        return template.render(code_model=self.code_model, **params)

    def serialize_serialization_file(self) -> str:
        template = self.env.get_template("serialization.py.jinja2")
        return template.render(code_model=self.code_model)
