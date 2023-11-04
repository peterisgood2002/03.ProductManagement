from .base_test import PMSDbTest
from .data import TestData, CheckData, Util

from pms_dbmodel.models.e_operator import EOperator, EComplianceVersion
from pms_dbmodel.models.e_operator_requirement import (
    EDocStructureCategory,
    EDocStructure,
)
from pms_dbmodel.operator_operation.doc_operation import DocOperation


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
        titleId = TestData.requirement_19[0][TestData.ARRAYINFO.ChapterId.value]
        title = TestData.requirement_19[0][TestData.ARRAYINFO.Chapter.value]
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

        sectionId = TestData.requirement_19[0][TestData.ARRAYINFO.SectionId.value]
        section = TestData.requirement_19[0][TestData.ARRAYINFO.Section.value]
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
