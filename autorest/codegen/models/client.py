# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from .base_model import BaseModel
from .parameter import Parameter
from .parameter_list import ClientGlobalParameterList, ConfigGlobalParameterList
from .imports import FileImport, ImportType, TypingSection

if TYPE_CHECKING:
    from .code_model import CodeModel


class Client(BaseModel):
    """A service client."""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        client_parameters: ClientGlobalParameterList,
        config_parameters: ConfigGlobalParameterList,
    ):
        super().__init__(yaml_data, code_model)
        self.client_parameters = client_parameters
        self.config_parameters = config_parameters
        self.name = self.yaml_data["name"]
        self.description = self.yaml_data["description"]
        self.url = self.yaml_data["url"]

    def pipeline_class(self, async_mode: bool) -> str:
        if self.code_model.options["azure_arm"]:
            if async_mode:
                return "AsyncARMPipelineClient"
            return "ARMPipelineClient"
        if async_mode:
            return "AsyncPipelineClient"
        return "PipelineClient"

    def _imports_shared(self, async_mode: bool) -> FileImport:
        file_import = FileImport()

        file_import.add_submodule_import("msrest", "Serializer", ImportType.THIRDPARTY)
        file_import.add_submodule_import(
            "msrest", "Deserializer", ImportType.THIRDPARTY
        )
        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL
        )

        any_optional_gp = any(not gp.required for gp in self.client_parameters)

        legacy = not any(
            g
            for g in ["low_level_client", "version_tolerant"]
            if g in self.code_model.options
        )
        if any_optional_gp or (
            legacy and self.code_model.client.parameters.host
        ):
            file_import.add_submodule_import(
                "typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL
            )

        if self.code_model.options["azure_arm"]:
            file_import.add_submodule_import(
                "azure.mgmt.core", self.pipeline_class(async_mode), ImportType.AZURECORE
            )
        else:
            file_import.add_submodule_import(
                "azure.core", self.pipeline_class(async_mode), ImportType.AZURECORE
            )

        for gp in self.code_model.global_parameters:
            file_import.merge(gp.imports())
        file_import.add_submodule_import(
            "._configuration",
            f"{self.code_model.client.name}Configuration",
            ImportType.LOCAL,
        )

        return file_import

    def imports(self, async_mode: bool) -> FileImport:
        file_import = self._imports_shared(async_mode)
        if async_mode:
            file_import.add_submodule_import("typing", "Awaitable", ImportType.STDLIB)
            file_import.add_submodule_import(
                "azure.core.rest",
                "AsyncHttpResponse",
                ImportType.AZURECORE,
                TypingSection.CONDITIONAL,
            )
        else:
            file_import.add_submodule_import(
                "azure.core.rest",
                "HttpResponse",
                ImportType.AZURECORE,
                TypingSection.CONDITIONAL,
            )
        file_import.add_submodule_import(
            "azure.core.rest",
            "HttpRequest",
            ImportType.AZURECORE,
            TypingSection.CONDITIONAL,
        )
        for og in self.code_model.operation_groups:
            file_import.add_submodule_import(
                f".{self.code_model.operations_folder_name}",
                og.class_name,
                ImportType.LOCAL,
            )

        if self.code_model.object_types:
            path_to_models = ".." if async_mode else "."
            file_import.add_submodule_import(path_to_models, "models", ImportType.LOCAL)
        else:
            # in this case, we have client_models = {} in the service client, which needs a type annotation
            # this import will always be commented, so will always add it to the typing section
            file_import.add_submodule_import(
                "typing", "Dict", ImportType.STDLIB, TypingSection.TYPING
            )
        file_import.add_submodule_import("copy", "deepcopy", ImportType.STDLIB)
        return file_import

    def imports_for_multiapi(self, async_mode: bool) -> FileImport:
        file_import = self._imports_shared(async_mode)
        try:
            mixin_operation = next(
                og
                for og in self.code_model.operation_groups
                if og.is_empty_operation_group
            )
            file_import.add_submodule_import(
                "._operations_mixin", mixin_operation.class_name, ImportType.LOCAL
            )
        except StopIteration:
            pass
        return file_import

    @property
    def filename(self) -> str:
        if (
            self.code_model.options["version_tolerant"]
            or self.code_model.options["low_level_client"]
        ):
            return "_client"
        return f"_{self.code_model.module_name}"

    @property
    def send_request_name(self) -> str:
        return "send_request" if self.code_model.options["show_send_request"] else "_send_request"

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "Client":
        parameters = [Parameter.from_yaml(p, code_model) for p in yaml_data["parameters"]]
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            client_parameters=ClientGlobalParameterList(code_model, parameters),
            config_parameters=ConfigGlobalParameterList(code_model, parameters)
        )
