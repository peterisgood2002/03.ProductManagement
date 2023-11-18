from pms_dbmodel.testoperatordata import TestOperatiorData, CheckOperatorData
from .base_test import PMSDbTest

from pms_dbmodel.models.e_operator import EOperator
from pms_dbmodel.operator_operation.operator_operation import OperatorOperation
from pms_dbmodel.operator_operation.requirement_operation import RequirementOperation


class OperatorOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            EOperator,
        )

    def testGetOperator(self):
        # 1. Insert ATT
        o = OperatorOperation.addOperator(
            TestOperatiorData.area, TestOperatiorData.operator1
        )
        CheckOperatorData.checkOperator(o, TestOperatiorData.operator1)

        o = OperatorOperation.getOperator(TestOperatiorData.operator1)
        CheckOperatorData.checkOperator(o, TestOperatiorData.operator1)
        o = OperatorOperation.getOperator(TestOperatiorData.operator2)
        assert o == None

        # 2. Insert TMO
        tmo = OperatorOperation.addOperator(
            TestOperatiorData.area, TestOperatiorData.operator2
        )
        CheckOperatorData.checkOperator(tmo, TestOperatiorData.operator2)

        # 3. Get TMO again
        o = OperatorOperation.addOperator(
            TestOperatiorData.area, TestOperatiorData.operator2
        )
        assert tmo == o
