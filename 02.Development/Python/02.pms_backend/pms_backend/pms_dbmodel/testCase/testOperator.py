from .base_test import PMSDbTest
from .data import TestData, CheckData

from pms_dbmodel.models.e_operator import EOperator
from pms_dbmodel.operator_operation.operator_operation import OperatorOperation


class OperatorOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            EOperator,
        )

    def testGetOperator(self):
        # 1. Insert ATT
        o = OperatorOperation.addOperator(TestData.area, TestData.operator1)
        CheckData.checkOperator(o, TestData.operator1)

        o = OperatorOperation.getOperator(TestData.operator1)
        CheckData.checkOperator(o, TestData.operator1)
        assert TestData.operator1 == o.name
        o = OperatorOperation.getOperator(TestData.operator2)
        assert o == None

        # 2. Insert TMO
        tmo = OperatorOperation.addOperator(TestData.area, TestData.operator2)
        CheckData.checkOperator(tmo, TestData.operator2)

        # 3. Get TMO again
        o = OperatorOperation.addOperator(TestData.area, TestData.operator2)
        assert tmo == o
