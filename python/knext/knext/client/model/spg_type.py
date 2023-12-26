# -*- coding: utf-8 -*-
# Copyright 2023 Ant Group CO., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

from typing import List, Dict, Union, Optional

from knext import rest
from knext.client.model.base import (
    BaseSpgType,
    SpgTypeEnum,
    ROOT_TYPE_UNIQUE_NAME,
    HypernymPredicateEnum,
    ConstraintTypeEnum,
)
from knext.client.model.property import Property
from knext.client.model.relation import Relation
from knext.operator.op import LinkOp, FuseOp


class EntityType(BaseSpgType):
    """EntityType Model."""

    spg_type_enum: SpgTypeEnum
    name: str
    name_zh: str
    desc: str
    parent_type_name: str
    properties: Dict[str, Property]
    relations: Dict[str, Relation]
    link_operator: LinkOp
    fuse_operator: FuseOp

    def __init__(
        self,
        name: str,
        name_zh: str = None,
        desc: str = None,
        parent_type_name: str = ROOT_TYPE_UNIQUE_NAME,
        properties: List[Property] = None,
        relations: List[Relation] = None,
        link_operator: LinkOp = None,
        fuse_operator: FuseOp = None,
        **kwargs,
    ):
        super().__init__(
            spg_type_enum=SpgTypeEnum.Entity,
            name=name,
            name_zh=name_zh,
            desc=desc,
            properties=properties,
            relations=relations,
            parent_type_name=parent_type_name,
            link_operator=link_operator,
            fuse_operator=fuse_operator,
            **kwargs,
        )
        if "rest_model" not in kwargs:
            self.link_operator = link_operator
            self.fuse_operator = fuse_operator

    @property
    def link_operator(self):
        """Gets the link_operator of this EntityType.  # noqa: E501


        :return: The link_operator of this EntityType.  # noqa: E501
        :rtype: Operator
        """
        if self._rest_model.advanced_config.link_operator is None:
            return None
        op_name = self._rest_model.advanced_config.link_operator.name
        op_version = self._rest_model.advanced_config.link_operator.version
        return self.link_operator.to_rest(op_name, op_version)

    @link_operator.setter
    def link_operator(self, link_operator: LinkOp):
        """Sets the link_operator of this EntityType.


        :param link_operator: The link_operator of this EntityType.  # noqa: E501
        :type: Operator
        """

        if link_operator is None:
            self._rest_model.advanced_config.link_operator = None
            return
        if self._rest_model.advanced_config.link_operator is None:
            self._rest_model.advanced_config.link_operator = rest.OperatorKey()
        self._rest_model.advanced_config.link_operator.name = link_operator.name
        self._rest_model.advanced_config.link_operator.version = link_operator._version

    def bind_link_operator(self, operator: LinkOp):
        """Binds a link operator to this EntityType."""

        self.link_operator = operator
        return self

    @property
    def fuse_operator(self):
        """Gets the fuse_operator of this EntityType.  # noqa: E501


        :return: The fuse_operator of this EntityType.  # noqa: E501
        :rtype: Operator
        """
        if self._rest_model.advanced_config.fuse_operator is None:
            return None
        op_name = self._rest_model.advanced_config.fuse_operator.name
        op_version = self._rest_model.advanced_config.fuse_operator.version
        return self.fuse_operator.to_rest(op_name, op_version)

    @fuse_operator.setter
    def fuse_operator(self, fuse_operator: FuseOp):
        """Sets the fuse_operator of this EntityType.


        :param fuse_operator: The fuse_operator of this EntityType.  # noqa: E501
        :type: Operator
        """

        if fuse_operator is None:
            self._rest_model.advanced_config.fuse_operator = None
            return
        if self._rest_model.advanced_config.fuse_operator is None:
            self._rest_model.advanced_config.fuse_operator = rest.OperatorKey()
        self._rest_model.advanced_config.fuse_operator.name = fuse_operator.name
        self._rest_model.advanced_config.fuse_operator.version = fuse_operator._version

    def bind_fuse_operator(self, operator: FuseOp):
        """Binds a fuse operator to this EntityType."""

        self.fuse_operator = operator
        return self


class ConceptType(BaseSpgType):
    """ConceptType Model."""

    spg_type_enum: SpgTypeEnum
    name: str
    hypernym_predicate: HypernymPredicateEnum
    name_zh: str
    desc: str
    parent_type_name: str
    properties: Dict[str, Property]
    relations: Dict[str, Relation]
    link_operator: LinkOp
    fuse_operator: FuseOp
    taxonomic_type_name: str

    def __init__(
        self,
        name: str,
        hypernym_predicate: HypernymPredicateEnum,
        name_zh: str = None,
        desc: str = None,
        parent_type_name: str = ROOT_TYPE_UNIQUE_NAME,
        properties: List[Property] = None,
        relations: List[Relation] = None,
        link_operator: LinkOp = None,
        taxonomic_type_name: str = None,
        **kwargs,
    ):
        super().__init__(
            spg_type_enum=SpgTypeEnum.Concept,
            name=name,
            name_zh=name_zh,
            desc=desc,
            properties=properties,
            relations=relations,
            parent_type_name=parent_type_name,
            **kwargs,
        )
        if "rest_model" not in kwargs:
            self.hypernym_predicate = hypernym_predicate
            self.taxonomic_type_name = taxonomic_type_name
            self.link_operator = link_operator

    @property
    def hypernym_predicate(self) -> Optional[HypernymPredicateEnum]:
        """Gets the hypernym_predicate of this ConceptType.  # noqa: E501


        :return: The hypernym_predicate of this ConceptType.  # noqa: E501
        :rtype: HypernymPredicateEnum
        """
        hypernym_predicate = self._rest_model.concept_layer_config.hypernym_predicate
        return HypernymPredicateEnum(hypernym_predicate) if hypernym_predicate else None

    @hypernym_predicate.setter
    def hypernym_predicate(self, hypernym_predicate: HypernymPredicateEnum):
        """Sets the hypernym_predicate of this ConceptType.


        :param hypernym_predicate: The hypernym_predicate of this ConceptType.  # noqa: E501
        :type: HypernymPredicateEnum
        """

        self._rest_model.concept_layer_config.hypernym_predicate = hypernym_predicate

    @property
    def taxonomic_type_name(self) -> Optional[str]:
        """Gets the taxonomic_type_name of this SpgType.  # noqa: E501


        :return: The taxonomic_type_name of this SpgType.  # noqa: E501
        :rtype: str
        """
        if self._rest_model.concept_taxonomic_config is None:
            return None
        return self._rest_model.concept_taxonomic_config.taxonomic_type_unique_name.name

    @taxonomic_type_name.setter
    def taxonomic_type_name(self, taxonomic_type_name: str):
        """Sets the taxonomic_type_name of this ConceptType.


        :param taxonomic_type_name: The taxonomic_type_name of this ConceptType.  # noqa: E501
        :type: str
        """
        if taxonomic_type_name is None:
            self._rest_model.concept_taxonomic_config = None
            return
        self._rest_model.concept_taxonomic_config.taxonomic_type_unique_name.name = (
            taxonomic_type_name
        )

    @property
    def link_operator(self):
        """Gets the link_operator of this ConceptType.  # noqa: E501


        :return: The link_operator of this ConceptType.  # noqa: E501
        :rtype: Operator
        """
        if self._rest_model.advanced_config.normalized_operator is None:
            return None
        op_name = self._rest_model.advanced_config.normalized_operator.name
        op_version = self._rest_model.advanced_config.normalized_operator.version
        return self.link_operator(op_name, op_version)

    @link_operator.setter
    def link_operator(self, link_operator: LinkOp):
        """Sets the link_operator of this ConceptType.


        :param link_operator: The link_operator of this ConceptType.  # noqa: E501
        :type: Operator
        """

        if link_operator is None:
            self._rest_model.advanced_config.normalized_operator = None
            return
        if self._rest_model.advanced_config.normalized_operator is None:
            self._rest_model.advanced_config.normalized_operator = rest.OperatorKey()
        self._rest_model.advanced_config.normalized_operator.name = link_operator.name
        self._rest_model.advanced_config.normalized_operator.version = (
            link_operator._version
        )

    def bind_link_operator(self, operator: LinkOp):
        """Binds a property normalize operator to this ConceptType."""

        self.link_operator = operator
        return self


class EventType(BaseSpgType):
    """EventType Model."""

    spg_type_enum: SpgTypeEnum
    name: str
    name_zh: str
    desc: str
    parent_type_name: str
    properties: Dict[str, Property]
    relations: Dict[str, Relation]
    link_operator: LinkOp

    def __init__(
        self,
        name: str,
        name_zh: str = None,
        desc: str = None,
        parent_type_name: str = ROOT_TYPE_UNIQUE_NAME,
        properties: List[Property] = None,
        relations: List[Relation] = None,
        link_operator: LinkOp = None,
        **kwargs,
    ):
        super().__init__(
            spg_type_enum=SpgTypeEnum.Event,
            name=name,
            name_zh=name_zh,
            desc=desc,
            properties=properties,
            relations=relations,
            parent_type_name=parent_type_name,
            **kwargs,
        )
        if "rest_model" not in kwargs:
            self.link_operator = link_operator

    @property
    def link_operator(self):
        """Gets the link_operator of this EventType.  # noqa: E501


        :return: The link_operator of this EventType.  # noqa: E501
        :rtype: Operator
        """
        if self._rest_model.advanced_config.link_operator is None:
            return None
        op_name = self._rest_model.advanced_config.normalized_operator.name
        op_version = self._rest_model.advanced_config.normalized_operator.version
        return self.link_operator(op_name, op_version)

    @link_operator.setter
    def link_operator(self, link_operator: LinkOp):
        """Sets the link_operator of this EventType.


        :param link_operator: The link_operator of this EventType.  # noqa: E501
        :type: Operator
        """

        if link_operator is None:
            self._rest_model.advanced_config.link_operator = None
            return
        if self._rest_model.advanced_config.link_operator is None:
            self._rest_model.advanced_config.link_operator = rest.OperatorKey()
        self._rest_model.advanced_config.link_operator.name = link_operator.name
        self._rest_model.advanced_config.link_operator.version = link_operator._version

    def bind_link_operator(self, operator: LinkOp):
        """Binds a link operator to this EventType."""

        self.link_operator = operator
        return self


class BasicType(BaseSpgType):
    """BasicType Model."""

    Text = BaseSpgType(SpgTypeEnum.Basic, "Text")
    Integer = BaseSpgType(SpgTypeEnum.Basic, "Integer")
    Float = BaseSpgType(SpgTypeEnum.Basic, "Float")

    def __init__(self, name: str, **kwargs):
        super().__init__(spg_type_enum=SpgTypeEnum.Basic, name=name, **kwargs)


class StandardType(BaseSpgType):
    """StandardType Model."""

    spg_type_enum: SpgTypeEnum
    name: str
    parent_type_name: str
    spreadable: bool
    constraint: Dict[ConstraintTypeEnum, Union[str, List[str]]]

    def __init__(
        self,
        name: str,
        parent_type_name: str = ROOT_TYPE_UNIQUE_NAME,
        spreadable: bool = False,
        constraint: Dict[ConstraintTypeEnum, Union[str, List[str]]] = None,
        **kwargs,
    ):
        super().__init__(
            spg_type_enum=SpgTypeEnum.Standard,
            name=name,
            parent_type_name=parent_type_name,
            spreadable=spreadable,
            constraint=constraint,
            **kwargs,
        )

    @property
    def spreadable(self) -> bool:
        """Gets the `spreadable` of this StandardType.  # noqa: E501


        :return: The `spreadable` of this StandardType.  # noqa: E501
        :rtype: bool
        """
        return self._rest_model.spreadable

    @spreadable.setter
    def spreadable(self, spreadable: bool):
        """Sets the `spreadable` of this StandardType.


        :param spreadable: The `spreadable` of this StandardType.  # noqa: E501
        :type: bool
        """
        self._rest_model.spreadable = spreadable

    @property
    def constraint(self) -> Dict[ConstraintTypeEnum, Union[str, list]]:
        """Gets the constraint of this StandardType.  # noqa: E501


        :return: The constraint of this StandardType.  # noqa: E501
        :rtype: dict
        """
        if self._rest_model.constraint_items is None:
            return {}
        constraint = {}
        for item in self._rest_model.constraint_items:
            if item.constraint_type_enum == ConstraintTypeEnum.Enum:
                value = item.enum_values
            elif item.constraint_type_enum == ConstraintTypeEnum.Regular:
                value = item.regular_pattern
            else:
                value = None
            constraint[item.constraint_type_enum] = value
        return constraint

    @constraint.setter
    def constraint(self, constraint: Dict[ConstraintTypeEnum, Union[str, list]]):
        """Sets the constraint of this StandardType.


        :param constraint: The constraint of this StandardType.  # noqa: E501
        :type: dict
        """
        if constraint is None:
            return
        self._rest_model.constraint_items = []
        for type, value in constraint.items():
            self.add_constraint(type, value)

    def add_constraint(self, type: ConstraintTypeEnum, value: Union[str, list] = None):
        """Adds a constraint to this StandardType.


        :param type: The type of constraint to add.
        :type type: ConstraintTypeEnum
        :param value: The value(s) of the constraint. Optional.
        :type value: str or list, optional
        """

        if self._rest_model.constraint_items is None:
            self._rest_model.constraint_items = []
        if type == ConstraintTypeEnum.Enum:
            if not isinstance(value, list):
                raise ValueError("Invalid enum format.")
            constraint_item = rest.EnumConstraint(enum_values=value)
        elif type == ConstraintTypeEnum.Regular:
            constraint_item = rest.RegularConstraint(regular_pattern=value)
        else:
            constraint_item = rest.BaseConstraintItem(type)
        self._rest_model.constraint_items.append(constraint_item)
        return self
