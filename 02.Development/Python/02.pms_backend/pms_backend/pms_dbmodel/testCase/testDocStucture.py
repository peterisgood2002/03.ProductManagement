from pms_dbmodel.tests import TestData, Util, CheckData
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

    def testInsertChapterAndSection(self):
        Util.addCategories()
        titleId = TestData.requirement_19[0].getInfo(OperatorRequirement.INFO.ChapterId)
        title = TestData.requirement_19[0].getInfo(OperatorRequirement.INFO.Chapter)
        [chapter, succeed] = DocOperation.addDocStructure(
            TestData.area,
            TestData.operator1,
            TestData.version19,
            TestData.categories[1],
            titleId,
            title,
        )
        assert succeed == True

        chapter = DocOperation.getDocStructure(
            TestData.operator1, TestData.version19, titleId
        )
        CheckData.checkDocStructure(
            chapter, TestData.operator1, TestData.version19, titleId, title, None
        )

        sectionId = TestData.requirement_19[0].getInfo(
            OperatorRequirement.INFO.SectionId
        )
        section = TestData.requirement_19[0].getInfo(OperatorRequirement.INFO.Section)
        [data, succeed] = DocOperation.addDocStructure(
            TestData.area,
            TestData.operator1,
            TestData.version19,
            TestData.categories[2],
            sectionId,
            section,
            chapter,
        )
        assert succeed == True
        data = DocOperation.getDocStructure(
            TestData.operator1, TestData.version19, sectionId
        )
        CheckData.checkDocStructure(
            data, TestData.operator1, TestData.version19, sectionId, section, chapter
        )
