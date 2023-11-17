from pms_dbmodel.tests import Util
from pms_dbmodel.testoperatordata import TestOperatiorData, CheckOperatorData
from .base_test import PMSDbTest

from pms_dbmodel.models.e_operator import EOperator, EComplianceVersion
from pms_dbmodel.models.e_operator_requirement import (
    EDocStructureCategory,
    EDocStructure,
)
from pms_dbmodel.operator_operation.doc_operation import DocOperation
from pms_dbmodel.operator import OperatorRequirement


class DocOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            EOperator,
            EComplianceVersion,
            EDocStructureCategory,
            EDocStructure,
        )

    def testGetCategoriesMap(self):
        Util.addCategories()
        result = DocOperation.getDocStructureCategoryMap()

        for c in TestOperatiorData.categories:
            assert c in result.keys()

    def testInsertChapterAndSection(self):
        Util.addCategories()
        titleId = TestOperatiorData.requirement_19[0].getInfo(
            OperatorRequirement.INFO.ChapterId
        )
        title = TestOperatiorData.requirement_19[0].getInfo(
            OperatorRequirement.INFO.Chapter
        )
        [chapter, succeed] = DocOperation.addDocStructure(
            TestOperatiorData.area,
            TestOperatiorData.operator1,
            TestOperatiorData.version19,
            TestOperatiorData.categories[1],
            titleId,
            title,
        )
        assert succeed == True

        chapter = DocOperation.getDocStructure(
            TestOperatiorData.operator1, TestOperatiorData.version19, titleId
        )
        CheckOperatorData.checkDocStructure(
            chapter,
            TestOperatiorData.operator1,
            TestOperatiorData.version19,
            titleId,
            title,
            None,
        )

        sectionId = TestOperatiorData.requirement_19[0].getInfo(
            OperatorRequirement.INFO.SectionId
        )
        section = TestOperatiorData.requirement_19[0].getInfo(
            OperatorRequirement.INFO.Section
        )
        [data, succeed] = DocOperation.addDocStructure(
            TestOperatiorData.area,
            TestOperatiorData.operator1,
            TestOperatiorData.version19,
            TestOperatiorData.categories[2],
            sectionId,
            section,
            chapter,
        )
        assert succeed == True
        data = DocOperation.getDocStructure(
            TestOperatiorData.operator1, TestOperatiorData.version19, sectionId
        )
        CheckOperatorData.checkDocStructure(
            data,
            TestOperatiorData.operator1,
            TestOperatiorData.version19,
            sectionId,
            section,
            chapter,
        )
