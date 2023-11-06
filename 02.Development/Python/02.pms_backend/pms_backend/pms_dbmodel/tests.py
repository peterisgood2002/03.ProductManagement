# Create your tests here.
from contextlib import contextmanager
from enum import Enum
from django.test import TestCase
from pms_dbmodel.operator import OperatorRequirement
from pms_dbmodel.models.e_operator import EComplianceVersion
from pms_dbmodel.models.e_operator import EOperator
from pms_dbmodel.operator_operation.doc_operation import DocOperation
from pms_dbmodel.models.e_operator import EArea
from pms_dbmodel.models.e_employee import EEmployee
from pms_dbmodel.models.e_operator_requirement import (
    EDocStructureCategory,
    EDocStructure,
    EDeviceRequirement,
    EDeviceRequirementDesc,
)
from pms_dbmodel.models.a_attribute import APriority

from django.db import models


class TestData:
    area = "NA"
    operator1 = "ATT"
    operator2 = "TMO"
    version19 = "19.3"
    version22 = "22.1"
    categories = ["Document", "Chapter", "Section"]

    requirement_19 = [
        OperatorRequirement(
            [
                version19,  # Version
                "1",  # ChapterId
                "Chapter 1",  # Chapter
                "1.1",  # SectionId
                "Section 1.1",  # Section
                "TAG_1",  # Tag
                "Requirement T1",  # Title
                "Requirement N1",  # Name
                "Requirement Desc1",  # Desc
            ]
        ),
        OperatorRequirement(
            [
                version19,  # Version
                "1",  # ChapterId
                "Chapter 1",  # Chapter
                "1.2",  # SectionId
                "Section 1.2",  # Section
                "TAG_2",  # Tag
                "Requirement T2",  # Title
                "Requirement N2",  # Name
                "Requirement Desc 2",  # Desc
            ]
        ),
        OperatorRequirement(
            [
                version19,  # Version
                "2",  # ChapterId
                "Chapter 2",  # Chapter
                "2.1",  # SectionId
                "Section 2.1",  # Section
                "TAG_3",  # Tag
                "Requirement T3",  # Title
                "Requirement N3",  # Name
                "Requirement Desc 3",  # Desc
            ]
        ),
    ]

    requirement_22_No = [
        OperatorRequirement(
            [
                version22,  # Version
                "2",  # ChapterId
                "Chapter 2",  # Chapter
                "2.1",  # SectionId
                "Section 2.1",  # Section
                "TAG_1",  # Tag
                "Requirement T1",  # Title
                "Requirement N1",  # Name
                "Requirement Desc1",  # Desc
            ]
        )
    ]


class Util:
    @staticmethod
    def addCategories():
        for c in TestData.categories:
            category = DocOperation.addDocStructureCategory(c)
            assert category.name == c


class CheckData:
    @staticmethod
    def checkOperator(operator, name):
        assert isinstance(operator, EOperator) == True
        assert operator.name == name
        assert int(operator.id / 100) == operator.area.id
        assert operator.area.name == TestData.area

    @staticmethod
    def checkVersion(version: EComplianceVersion, operator, version_no):
        assert version.version_no == version_no
        CheckData.checkOperator(version.operator, operator)

    @staticmethod
    def checkDocStructure(
        data: EDocStructure,
        operator,
        verison,
        id,
        title,
        parent_id: EDocStructure,
    ):
        CheckData.checkOperator(data.operator, operator)
        CheckData.checkVersion(data.version, operator, verison)
        assert data.doc_id == id
        assert data.name == title

        if parent_id != None:
            assert data.parent_structure_id == parent_id.doc_id

    @staticmethod
    def checkDeviceRequirmentDesc(data: EDeviceRequirementDesc, title, name, desc=""):
        assert data.title == title
        assert data.name == name
        assert data.description == desc

    @staticmethod
    def checkDeviceRequirement(
        data: EDeviceRequirement, operator, reference: OperatorRequirement
    ):
        CheckData.checkOperator(data.operator, operator)
        CheckData.checkVersion(
            data.version, operator, reference.getInfo(OperatorRequirement.INFO.VERSION)
        )

        CheckData.checkDeviceRequirmentDesc(
            data.descId,
            reference.getInfo(OperatorRequirement.INFO.TITLE),
            reference.getInfo(OperatorRequirement.INFO.NAME),
            reference.getInfo(OperatorRequirement.INFO.DESC),
        )
        assert data.tag_id == reference.getInfo(OperatorRequirement.INFO.TAG)

    @staticmethod
    def checkNoChangeDeviceRequirement(
        data: EDeviceRequirement, operator, tag_id: str, reference, preData: dict
    ):
        CheckData.checkDeviceRequirement(data, operator, reference)

        descId = preData[tag_id].descId
        assert isinstance(descId, EDeviceRequirementDesc) == True
        assert data.descId == descId
