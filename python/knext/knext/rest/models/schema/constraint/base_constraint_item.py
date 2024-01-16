# coding: utf-8
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.


"""
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from knext.rest.configuration import Configuration


class BaseConstraintItem(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"constraint_type_enum": "str"}

    attribute_map = {"constraint_type_enum": "constraintTypeEnum"}

    discriminator_value_class_map = {
        "ENUM": "EnumConstraint",
        "MULTI_VALUE": "MultiValConstraint",
        "NOT_NULL": "NotNullConstraint",
        "REGULAR": "RegularConstraint",
    }

    def __init__(
        self, constraint_type_enum=None, local_vars_configuration=None
    ):  # noqa: E501
        """BaseConstraintItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._constraint_type_enum = None
        self.discriminator = constraint_type_enum

        self.constraint_type_enum = constraint_type_enum

    @property
    def constraint_type_enum(self):
        """Gets the constraint_type_enum of this BaseConstraintItem.  # noqa: E501


        :return: The constraint_type_enum of this BaseConstraintItem.  # noqa: E501
        :rtype: str
        """
        return self._constraint_type_enum

    @constraint_type_enum.setter
    def constraint_type_enum(self, constraint_type_enum):
        """Sets the constraint_type_enum of this BaseConstraintItem.


        :param constraint_type_enum: The constraint_type_enum of this BaseConstraintItem.  # noqa: E501
        :type: str
        """

        allowed_values = [
            None,
            "NOT_NULL",
            "MULTI_VALUE",
            "ENUM",
            "REGULAR",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and constraint_type_enum not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `constraint_type_enum` ({0}), must be one of {1}".format(  # noqa: E501
                    constraint_type_enum, allowed_values
                )
            )

        self._constraint_type_enum = constraint_type_enum

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def get_real_child_model(self, data):
        """Returns the child model by discriminator"""
        if "@type" in data:
            child_type = data.get("@type")
            real_child_model = self.discriminator_value_class_map.get(child_type)
            return real_child_model
        return None

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BaseConstraintItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseConstraintItem):
            return True

        return self.to_dict() != other.to_dict()
