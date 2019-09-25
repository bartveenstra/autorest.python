# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from .modeltype import ModelType
from typing import Any, Dict, List
from ..common.utils import to_python_type


class CompositeType(ModelType):
    """Represents a composite type schema ready to be serialized in Python.

    :param str name: The name of the composite type.
    :param str description: The description of the composite type.
    :param properties: the optional properties of the composite thpe.
    :type properties: dict(str, str)
    """
    def __init__(self, name: str, description: str, **kwargs: "**Any") -> "CompositeType":
        super(CompositeType, self).__init__(name, description, **kwargs)
        self.properties = kwargs.pop('properties', None)
        self.base_model = kwargs.pop('base_model', None)
        self.property_type = kwargs.pop('property_type', None)
        self.property_documentation_string = None
        self.init_line = None
        self.init_args = None

    def get_attribute_map_type(self) -> str:
        return self.property_type

    def _get_property_type_from_yaml(yaml_data):
        # checks to see if it's a top level CompositeType and not a property
        if yaml_data.get('properties'):
            return None
        schema_data = yaml_data['schema']
        property_type = schema_data['type']
        # all of is inheritance
        if property_type == 'object':
            # TODO: make sure pure objects don't have $key entry
            if schema_data.get('$key'):
                # property is of a class in our yaml file
                return schema_data['$key']
            # if not, the property's type is just object
            return property_type
        return to_python_type(property_type)

    """Returns the properties of a CompositeType if they exist.

    :param yaml_data: a dictionary object representative of the yaml schema
    for the composite type.
    :type yaml_data: dict(str, str)
    :returns: a list of the properties of the composite type
    :rtype: list[~autorest.models.Property or
     ~autorest.models.DictionaryType or
     ~autorest.models.SequenceType or
     ~autorest.models.EnumType]
    """
    @classmethod
    def _create_properties(cls, yaml_data: Dict[str, str]) -> List["Property"]:
        properties = []
        for prop in yaml_data['properties']:
            from . import build_property
            properties.append(build_property(prop))
        return properties

    """Returns a CompositeType from the dict object constructed from a yaml file.

    :param str name: The name of the composite type.
    :param yaml_data: A representation of the schema of a composite type from a yaml file.
    :type yaml_data: dict(str, str)
    :returns: A CompositeType.
    :rtype: ~autorest.models.schema.CompositeType
    """
    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs) -> "CompositeType":
        # Returns a CompositeType from a yaml file
        name = kwargs.pop('name', None)
        is_parent = kwargs.pop('is_parent', False)
        child_composite_types = kwargs.pop('child_composite_types', [])
        if not name:
            name = yaml_data['language']['default']['name']
        description = yaml_data['description'].strip() or (name + ".")
        if description == "MISSING-SCHEMA-DESCRIPTION-OBJECTSCHEMA":
            description = name + "."
        properties = cls._create_properties(yaml_data) if yaml_data.get('properties') else None
        base_model = None
        # if not is_parent:
        #     for p in child_composite_types:
        #         if name == p['language']['default']['name']:
        #             base_model = cls.from_yaml(p['allOf'][-1], is_parent=True)
        required = yaml_data.get('required')
        readonly = yaml_data.get('readOnly')
        constant = yaml_data.get('constant')
        property_type = cls._get_property_type_from_yaml(yaml_data)
        return cls(
            name=name,
            description=description,
            properties=properties,
            base_model=base_model,
            property_type=property_type,
            required=required,
            readonly=readonly,
            constant=constant
        )