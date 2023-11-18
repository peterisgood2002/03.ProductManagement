from pms_dbmodel.tests import Util
from pms_dbmodel.testoperatordata import TestOperatiorData, CheckOperatorData
from pms_dbmodel.operator_operation.doc_operation import DocOperation
from .base_test import PMSDbTest, logger

from pms_dbmodel.models.e_operator import EOperator, EComplianceVersion
from pms_dbmodel.models.e_operator_requirement import (
    EDeviceRequirementDesc,
    EDeviceRequirement,
    EDocStructureCategory,
    EDocStructure,
    ERequirementCategory,
    RDeviceRequirementCategory,
)

from pms_dbmodel.models.a_attribute import APriority
from pms_dbmodel.operator_operation.requirement_operation import RequirementOperation
from pms_dbmodel.common import logInfo, LOGTIME

from pms_dbmodel.operator import OperatorRequirement


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
            ERequirementCategory,
            RDeviceRequirementCategory,
        )

    def testInsertDeviceRequirementDesc(self):
        # 1. New a requirement

        requirement = TestOperatiorData.requirement_19[0]
        [data, success] = RequirementOperation.addDeviceRequirementDesc(
            requirement.getInfo(OperatorRequirement.INFO.TITLE),
            requirement.getInfo(OperatorRequirement.INFO.NAME),
            requirement.getInfo(OperatorRequirement.INFO.DESC),
        )
        assert success == True
        result = RequirementOperation.getDeviceRequirementDesc(data.id)
        CheckOperatorData.checkDeviceRequirmentDesc(
            result,
            requirement.getInfo(OperatorRequirement.INFO.TITLE),
            requirement.getInfo(OperatorRequirement.INFO.NAME),
            requirement.getInfo(OperatorRequirement.INFO.DESC),
        )

        rList = RequirementOperation.getDeviceRequirmentDecList(
            requirement.getInfo(OperatorRequirement.INFO.TITLE),
            requirement.getInfo(OperatorRequirement.INFO.NAME),
            requirement.getInfo(OperatorRequirement.INFO.DESC),
        )
        assert 1 == len(rList)

    def testInsertNewRequirement(self):
        for req in TestOperatiorData.requirement_19:
            r = RequirementOperation.addNewDeviceRequirement(
                TestOperatiorData.area,
                TestOperatiorData.operator1,
                req.getInfo(OperatorRequirement.INFO.VERSION),
                None,
                req.getInfo(OperatorRequirement.INFO.TAG),
                req.getInfo(OperatorRequirement.INFO.TITLE),
                req.getInfo(OperatorRequirement.INFO.NAME),
                req.getInfo(OperatorRequirement.INFO.DESC),
            )

            result = RequirementOperation.getDeviceRequirement(
                TestOperatiorData.operator1,
                req.getInfo(OperatorRequirement.INFO.VERSION),
                req.getInfo(OperatorRequirement.INFO.TAG),
            )

            CheckOperatorData.checkDeviceRequirement(
                result, TestOperatiorData.operator1, req
            )
        assert (
            len(TestOperatiorData.requirement_19)
            == EDeviceRequirementDesc.objects.count()
        )
        rList = RequirementOperation.getDeviceRequirementList(
            TestOperatiorData.operator1, TestOperatiorData.version19
        )
        assert len(TestOperatiorData.requirement_19) == len(rList)

        self._testInsertNoChangeRequirement()

    def _testInsertNoChangeRequirement(self):
        logInfo(logger, LOGTIME.BEGIN, self._testInsertNoChangeRequirement.__name__)
        Util.addDocCategories()

        # Create a version with the same requirement based on TAG
        rMap = RequirementOperation.getDeviceRequirementMapBasedOnTagId(
            TestOperatiorData.operator1, TestOperatiorData.version19
        )

        for req in TestOperatiorData.requirement_22_No:
            [section, succeed] = DocOperation.addDocStructure(
                TestOperatiorData.area,
                TestOperatiorData.operator1,
                req.getInfo(OperatorRequirement.INFO.VERSION),
                TestOperatiorData.categories[2],
                req.getInfo(OperatorRequirement.INFO.SectionId),
                req.getInfo(OperatorRequirement.INFO.Section),
                None,
            )
            [result, succeed] = RequirementOperation.addNoChangeDeviceRequirement(
                TestOperatiorData.area,
                TestOperatiorData.operator1,
                req.getInfo(OperatorRequirement.INFO.VERSION),
                section,
                req.getInfo(OperatorRequirement.INFO.TAG),
                rMap,
            )

            result = RequirementOperation.getDeviceRequirement(
                TestOperatiorData.operator1,
                req.getInfo(OperatorRequirement.INFO.VERSION),
                req.getInfo(OperatorRequirement.INFO.TAG),
            )
            CheckOperatorData.checkNoChangeDeviceRequirement(
                result,
                TestOperatiorData.operator1,
                req.getInfo(OperatorRequirement.INFO.TAG),
                req,
                rMap,
            )

        assert (
            len(TestOperatiorData.requirement_19)
            == EDeviceRequirementDesc.objects.count()
        )
        rList = RequirementOperation.getDeviceRequirementList(
            TestOperatiorData.operator1, TestOperatiorData.version22
        )
        assert 1 == len(rList)
        logInfo(logger, LOGTIME.END, self._testInsertNoChangeRequirement.__name__)

        req = TestOperatiorData.requirement_22_No[0]
        category = RequirementOperation.addCategoryWithTagId(
            TestOperatiorData.operator1,
            req.getInfo(OperatorRequirement.INFO.VERSION),
            req.getInfo(OperatorRequirement.INFO.TAG),
            "TEST",
        )

        category = RequirementOperation.addCategoryWithTagId(
            TestOperatiorData.operator1,
            req.getInfo(OperatorRequirement.INFO.VERSION),
            req.getInfo(OperatorRequirement.INFO.TAG),
            "TEST2",
        )

        categories = RequirementOperation.getCategories(
            TestOperatiorData.operator1,
            req.getInfo(OperatorRequirement.INFO.VERSION),
            req.getInfo(OperatorRequirement.INFO.TAG),
        )
        assert 2 == len(categories)
        assert "TEST" in categories
        assert "TEST2" in categories
