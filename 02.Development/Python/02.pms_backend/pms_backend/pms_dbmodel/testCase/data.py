from pms_dbmodel.models.e_operator import EOperator, EComplianceVersion
from pms_dbmodel.models.e_operator_requirement import (
    EDocStructure,
    EDeviceRequirementDesc,
    EDeviceRequirement,
)
from pms_dbmodel.operator_operation.doc_operation import DocOperation
from enum import Enum


class TestData:
    area = "NA"
    operator1 = "ATT"
    operator2 = "TMO"
    version19 = "19.3"
    version22 = "22.1"
    categories = ["Document", "Chapter", "Section"]

    class ARRAYINFO(Enum):
        VERSION = 0
        ChapterId = 1
        Chapter = 2
        SectionId = 3
        Section = 4
        TAG = 5
        TITLE = 6
        NAME = 7
        DESC = 8

    requirement_19 = [
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
        ],
        [
            version19,  # Version
            "1",  # ChapterId
            "Chapter 1",  # Chapter
            "1.2",  # SectionId
            "TEST 2",  # Section
            "TAG_2",  # Tag
            "Requirement T2",  # Title
            "Requirement N2",  # Name
            "Requirement Desc 2",  # Desc
        ],
    ]

    requirement_22_No = [
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
    def checkDeviceRequirement(data: EDeviceRequirement, operator, reference: list):
        CheckData.checkOperator(data.operator, operator)
        CheckData.checkVersion(
            data.version, operator, reference[TestData.ARRAYINFO.VERSION.value]
        )

        CheckData.checkDeviceRequirmentDesc(
            data.descId,
            reference[TestData.ARRAYINFO.TITLE.value],
            reference[TestData.ARRAYINFO.NAME.value],
            reference[TestData.ARRAYINFO.DESC.value],
        )
        assert data.tag_id == reference[TestData.ARRAYINFO.TAG.value]

    @staticmethod
    def checkNoChangeDeviceRequirement(
        data: EDeviceRequirement, operator, tag_id: str, reference, preData: dict
    ):
        CheckData.checkDeviceRequirement(data, operator, reference)

        descId = preData[tag_id].descId
        assert isinstance(descId, EDeviceRequirementDesc) == True
        assert data.descId == descId
