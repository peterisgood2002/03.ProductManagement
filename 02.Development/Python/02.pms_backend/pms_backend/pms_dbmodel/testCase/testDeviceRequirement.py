from .base_test import PMSDbTest, logger
from .data import TestData, CheckData, Util

from pms_dbmodel.models.e_operator import EOperator, EComplianceVersion
from pms_dbmodel.models.e_operator_requirement import (
    EDeviceRequirementDesc,
    EDeviceRequirement,
    EDocStructureCategory,
    EDocStructure,
)

from pms_dbmodel.models.a_attribute import APriority
from pms_dbmodel.operator_models import RequirementOperation, DocOperation
from pms_dbmodel.common import logInfo, LOGTIME


class RequirementOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            EOperator,
            EComplianceVersion,
            EDeviceRequirementDesc,
            EDeviceRequirement,
            APriority,
            EDocStructureCategory,
            EDocStructure,
        )

    def testInsertDeviceRequirementDesc(self):
        # 1. New a requirement

        requirement = TestData.requirement_19[0]
        [data, success] = RequirementOperation.addDeviceRequirementDesc(
            requirement[TestData.ARRAYINFO.TITLE.value],
            requirement[TestData.ARRAYINFO.NAME.value],
            requirement[TestData.ARRAYINFO.DESC.value],
        )
        assert success == True
        result = RequirementOperation.getDeviceRequirementDesc(data.id)
        CheckData.checkDeviceRequirmentDesc(
            result,
            requirement[TestData.ARRAYINFO.TITLE.value],
            requirement[TestData.ARRAYINFO.NAME.value],
            requirement[TestData.ARRAYINFO.DESC.value],
        )

        rList = RequirementOperation.getDeviceRequirmentDecList(
            requirement[TestData.ARRAYINFO.TITLE.value],
            requirement[TestData.ARRAYINFO.NAME.value],
            requirement[TestData.ARRAYINFO.DESC.value],
        )
        assert 1 == len(rList)

    def testInsertNewRequirement(self):
        for req in TestData.requirement_19:
            r = RequirementOperation.addNewDeviceRequirement(
                TestData.area,
                TestData.operator1,
                req[TestData.ARRAYINFO.VERSION.value],
                None,
                req[TestData.ARRAYINFO.TAG.value],
                req[TestData.ARRAYINFO.TITLE.value],
                req[TestData.ARRAYINFO.NAME.value],
                req[TestData.ARRAYINFO.DESC.value],
            )

            result = RequirementOperation.getDeviceRequirement(
                TestData.operator1,
                req[TestData.ARRAYINFO.VERSION.value],
                req[TestData.ARRAYINFO.TAG.value],
            )

            CheckData.checkDeviceRequirement(result, TestData.operator1, req)
        assert 2 == EDeviceRequirementDesc.objects.count()
        rList = RequirementOperation.getDeviceRequirementList(
            TestData.operator1, TestData.version19
        )
        assert 2 == len(rList)

        self._testInsertNoChangeRequirement()

    def _testInsertNoChangeRequirement(self):
        logInfo(logger, LOGTIME.BEGIN, self._testInsertNoChangeRequirement.__name__)
        Util.addCategories()

        # Create a version with the same requirement based on TAG
        rMap = RequirementOperation.getDeviceRequirementMapBasedOnTagId(
            TestData.operator1, TestData.version19
        )

        for req in TestData.requirement_22_No:
            [section, succeed] = DocOperation.addDocStructure(
                TestData.area,
                TestData.operator1,
                req[TestData.ARRAYINFO.VERSION.value],
                TestData.categories[2],
                req[TestData.ARRAYINFO.SectionId.value],
                req[TestData.ARRAYINFO.Section.value],
                None,
            )
            [result, succeed] = RequirementOperation.addNoChangeDeviceRequirement(
                TestData.area,
                TestData.operator1,
                req[TestData.ARRAYINFO.VERSION.value],
                section,
                req[TestData.ARRAYINFO.TAG.value],
                rMap,
            )

            result = RequirementOperation.getDeviceRequirement(
                TestData.operator1,
                req[TestData.ARRAYINFO.VERSION.value],
                req[TestData.ARRAYINFO.TAG.value],
            )
            CheckData.checkNoChangeDeviceRequirement(
                result,
                TestData.operator1,
                req[TestData.ARRAYINFO.TAG.value],
                req,
                rMap,
            )

        assert 2 == EDeviceRequirementDesc.objects.count()
        rList = RequirementOperation.getDeviceRequirementList(
            TestData.operator1, TestData.version22
        )
        assert 1 == len(rList)
        logInfo(logger, LOGTIME.END, self._testInsertNoChangeRequirement.__name__)
