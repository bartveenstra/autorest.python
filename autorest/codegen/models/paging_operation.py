# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, List, Any, Optional

from .operation import Operation
from .parameter import Parameter
from .schema_response import SchemaResponse
from .imports import ImportType

_LOGGER = logging.getLogger(__name__)


class PagingOperation(Operation):

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        description: str,
        url: str,
        method: str,
        parameters: List[Parameter] = None,
        responses: List[SchemaResponse] = None,
        exceptions: List[SchemaResponse] = None,
        media_types: List[str] = None,
    ) -> None:
        super(PagingOperation, self).__init__(
            yaml_data,
            name,
            description,
            url,
            method,
            parameters,
            responses,
            exceptions,
            media_types
        )
        self._item_name = yaml_data['extensions']['x-ms-pageable'].get("itemName")
        self._next_link_name = yaml_data['extensions']['x-ms-pageable'].get("nextLinkName")
        self.operation_name = yaml_data['extensions']['x-ms-pageable'].get("operationName")
        self.next_operation: Optional[Operation] = None

    def _find_python_name(self, rest_api_name, log_name):
        response = self.responses[0]
        for prop in response.schema.properties:
            if prop.original_swagger_name == rest_api_name:
                return prop.name
        raise ValueError(
            f"While scanning x-ms-pageable, was unable to find " +
            f"{log_name}:{rest_api_name} in model {response.schema.name}"
        )

    @property
    def item_name(self):
        if self._item_name is None:
            # Default value. I still check if I find it,  so I can do a nice message.
            item_name = "value"
            try:
                self._find_python_name(item_name, "itemName")
            except ValueError:
                response = self.responses[0]
                raise ValueError(
                    f"While scanning x-ms-pageable, itemName was not defined " +
                     f"and object {response.schema.name} has no array called 'value'"
                )
            return item_name
        return self._find_python_name(self._item_name, "itemName")

    @property
    def next_link_name(self):
        if not self._next_link_name:
            # That's an ok scenario, it just means no next page possible
            return None
        return self._find_python_name(self._next_link_name, "nextLinkName")

    def imports(self, code_model, async_mode):
        file_import = super(PagingOperation, self).imports(code_model, async_mode)

        if async_mode:
            file_import.add_from_import(
                "azure.core.async_paging", "AsyncItemPaged", ImportType.AZURECORE
            )
            file_import.add_from_import(
                "azure.core.async_paging", "AsyncList", ImportType.AZURECORE
            )
        else:
            file_import.add_from_import(
                "azure.core.paging", "ItemPaged", ImportType.AZURECORE
            )

        if code_model.options['tracing']:
            file_import.add_from_import(
                "azure.core.tracing.decorator",
                "distributed_trace",
                ImportType.AZURECORE,
            )

        return file_import
