# coding: utf-8
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


# flake8: noqa

"""
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

__version__ = "1"

from knext.rest.api.builder_api import BuilderApi
from knext.rest.api.concept_api import ConceptApi

# import apis into sdk package
from knext.rest.api.editor_api import EditorApi
from knext.rest.api.object_store_api import ObjectStoreApi
from knext.rest.api.operator_api import OperatorApi
from knext.rest.api.project_api import ProjectApi
from knext.rest.api.reasoner_api import ReasonerApi
from knext.rest.api.schema_api import SchemaApi
from knext.rest.api.table_store_api import TableStoreApi

# import ApiClient
from knext.rest.api_client import ApiClient
from knext.rest.api_client import BaseApi
from knext.rest.configuration import Configuration
from knext.rest.exceptions import ApiException
from knext.rest.exceptions import ApiKeyError
from knext.rest.exceptions import ApiTypeError
from knext.rest.exceptions import ApiValueError
from knext.rest.exceptions import OpenApiException
from knext.rest.models.builder.pipeline.config.base_node_config import BaseNodeConfig
from knext.rest.models.builder.pipeline.config.csv_source_node_config import (
    CsvSourceNodeConfig,
)
from knext.rest.models.builder.pipeline.config.graph_store_sink_node_config import (
    GraphStoreSinkNodeConfig,
)
from knext.rest.models.builder.pipeline.config.mapping_config import MappingConfig
from knext.rest.models.builder.pipeline.config.mapping_filter import MappingFilter
from knext.rest.models.builder.pipeline.config.operator_config import OperatorConfig
from knext.rest.models.builder.pipeline.edge import Edge
from knext.rest.models.builder.pipeline.node import Node
from knext.rest.models.builder.pipeline.pipeline import Pipeline
from knext.rest.models.builder.request.builder_job_submit_request import (
    BuilderJobSubmitRequest,
)
from knext.rest.models.builder.response.base_builder_receipt import BaseBuilderReceipt
from knext.rest.models.builder.response.base_builder_result import BaseBuilderResult
from knext.rest.models.builder.response.builder_job_inst import BuilderJobInst
from knext.rest.models.builder.response.failure_builder_result import (
    FailureBuilderResult,
)
from knext.rest.models.builder.response.job_builder_receipt import JobBuilderReceipt
from knext.rest.models.builder.response.success_builder_result import (
    SuccessBuilderResult,
)

# import models into sdk package
from knext.rest.models.common.user_info import UserInfo
from knext.rest.models.operator.operator_overview import OperatorOverview
from knext.rest.models.operator.operator_version import OperatorVersion
from knext.rest.models.reasoner.request.base_reasoner_content import BaseReasonerContent
from knext.rest.models.reasoner.request.kgdsl_reasoner_content import (
    KgdslReasonerContent,
)
from knext.rest.models.reasoner.request.reasoner_dsl_run_request import (
    ReasonerDslRunRequest,
)
from knext.rest.models.reasoner.request.reasoner_job_submit_request import (
    ReasonerJobSubmitRequest,
)
from knext.rest.models.reasoner.request.vertex_reasoner_content import (
    VertexReasonerContent,
)
from knext.rest.models.reasoner.response.base_reasoner_receipt import (
    BaseReasonerReceipt,
)
from knext.rest.models.reasoner.response.base_reasoner_result import BaseReasonerResult
from knext.rest.models.reasoner.response.failure_reasoner_result import (
    FailureReasonerResult,
)
from knext.rest.models.reasoner.response.job_reasoner_receipt import JobReasonerReceipt
from knext.rest.models.reasoner.response.reasoner_job_inst import ReasonerJobInst
from knext.rest.models.reasoner.response.success_reasoner_result import (
    SuccessReasonerResult,
)
from knext.rest.models.reasoner.response.table_reasoner_receipt import (
    TableReasonerReceipt,
)
from knext.rest.models.reasoner.starting_vertex import StartingVertex
from knext.rest.models.request.define_dynamic_taxonomy_request import (
    DefineDynamicTaxonomyRequest,
)
from knext.rest.models.request.define_logical_causation_request import (
    DefineLogicalCausationRequest,
)
from knext.rest.models.request.operator_create_request import OperatorCreateRequest
from knext.rest.models.request.operator_version_request import OperatorVersionRequest
from knext.rest.models.request.project_create_request import ProjectCreateRequest
from knext.rest.models.request.remove_dynamic_taxonomy_request import (
    RemoveDynamicTaxonomyRequest,
)
from knext.rest.models.request.remove_logical_causation_request import (
    RemoveLogicalCausationRequest,
)
from knext.rest.models.request.schema_alter_request import SchemaAlterRequest
from knext.rest.models.response.object_store_response import ObjectStoreResponse
from knext.rest.models.response.operator_create_response import OperatorCreateResponse
from knext.rest.models.response.operator_version_response import OperatorVersionResponse
from knext.rest.models.response.project import Project
from knext.rest.models.response.search_engine_index_response import (
    SearchEngineIndexResponse,
)
from knext.rest.models.schema.alter.schema_draft import SchemaDraft
from knext.rest.models.schema.base_ontology import BaseOntology
from knext.rest.models.schema.basic_info import BasicInfo
from knext.rest.models.schema.constraint.base_constraint_item import BaseConstraintItem
from knext.rest.models.schema.constraint.constraint import Constraint
from knext.rest.models.schema.constraint.enum_constraint import EnumConstraint
from knext.rest.models.schema.constraint.multi_val_constraint import MultiValConstraint
from knext.rest.models.schema.constraint.not_null_constraint import NotNullConstraint
from knext.rest.models.schema.constraint.regular_constraint import RegularConstraint
from knext.rest.models.schema.identifier.base_spg_identifier import BaseSpgIdentifier
from knext.rest.models.schema.identifier.concept_identifier import ConceptIdentifier
from knext.rest.models.schema.identifier.operator_identifier import OperatorIdentifier
from knext.rest.models.schema.identifier.predicate_identifier import PredicateIdentifier
from knext.rest.models.schema.identifier.spg_triple_identifier import (
    SpgTripleIdentifier,
)
from knext.rest.models.schema.identifier.spg_type_identifier import SpgTypeIdentifier
from knext.rest.models.schema.ontology_id import OntologyId
from knext.rest.models.schema.predicate.mounted_concept_config import (
    MountedConceptConfig,
)
from knext.rest.models.schema.predicate.property import Property
from knext.rest.models.schema.predicate.property_advanced_config import (
    PropertyAdvancedConfig,
)
from knext.rest.models.schema.predicate.property_ref import PropertyRef
from knext.rest.models.schema.predicate.property_ref_basic_info import (
    PropertyRefBasicInfo,
)
from knext.rest.models.schema.predicate.relation import Relation
from knext.rest.models.schema.predicate.sub_property import SubProperty
from knext.rest.models.schema.predicate.sub_property_basic_info import (
    SubPropertyBasicInfo,
)
from knext.rest.models.schema.semantic.base_semantic import BaseSemantic
from knext.rest.models.schema.semantic.logical_rule import LogicalRule
from knext.rest.models.schema.semantic.predicate_semantic import PredicateSemantic
from knext.rest.models.schema.semantic.rule_code import RuleCode
from knext.rest.models.schema.type.base_advanced_type import BaseAdvancedType
from knext.rest.models.schema.type.base_spg_type import BaseSpgType
from knext.rest.models.schema.type.basic_type import BasicType
from knext.rest.models.schema.type.concept_layer_config import ConceptLayerConfig
from knext.rest.models.schema.type.concept_taxonomic_config import (
    ConceptTaxonomicConfig,
)
from knext.rest.models.schema.type.concept_type import ConceptType
from knext.rest.models.schema.type.entity_type import EntityType
from knext.rest.models.schema.type.event_type import EventType
from knext.rest.models.schema.type.multi_version_config import MultiVersionConfig
from knext.rest.models.schema.type.operator_key import OperatorKey
from knext.rest.models.schema.type.parent_type_info import ParentTypeInfo
from knext.rest.models.schema.type.project_schema import ProjectSchema
from knext.rest.models.schema.type.spg_type_advanced_config import SpgTypeAdvancedConfig
from knext.rest.models.schema.type.spg_type_ref import SpgTypeRef
from knext.rest.models.schema.type.spg_type_ref_basic_info import SpgTypeRefBasicInfo
from knext.rest.models.schema.type.standard_type import StandardType
from knext.rest.models.schema.type.standard_type_basic_info import StandardTypeBasicInfo
from knext.rest.models.builder.pipeline.config.llm_based_extract_node_config import (
    LlmBasedExtractNodeConfig,
)
from knext.rest.models.builder.pipeline.config.relation_mapping_node_config import (
    RelationMappingNodeConfig,
)
from knext.rest.models.builder.pipeline.config.spg_type_mapping_node_config import (
    SpgTypeMappingNodeConfig,
)
from knext.rest.models.builder.pipeline.config.sub_graph_mapping_node_config import (
    SubGraphMappingNodeConfig,
)
from knext.rest.models.builder.pipeline.config.user_defined_extract_node_config import (
    UserDefinedExtractNodeConfig,
)
from knext.rest.models.builder.pipeline.config.base_fusing_config import (
    BaseFusingConfig,
)
from knext.rest.models.builder.pipeline.config.base_linking_config import (
    BaseLinkingConfig,
)
from knext.rest.models.builder.pipeline.config.base_predicting_config import (
    BasePredictingConfig,
)
from knext.rest.models.builder.pipeline.config.base_strategy_config import (
    BaseStrategyConfig,
)
from knext.rest.models.builder.pipeline.config.id_equals_linking_config import (
    IdEqualsLinkingConfig,
)
from knext.rest.models.builder.pipeline.config.operator_fusing_config import (
    OperatorFusingConfig,
)
from knext.rest.models.builder.pipeline.config.operator_linking_config import (
    OperatorLinkingConfig,
)
from knext.rest.models.builder.pipeline.config.operator_predicting_config import (
    OperatorPredictingConfig,
)
from knext.rest.models.builder.pipeline.config.predicting_config import PredictingConfig
from knext.rest.models.builder.pipeline.config.new_instance_fusing_config import (
    NewInstanceFusingConfig,
)
