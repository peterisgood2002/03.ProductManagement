from .base_test import PMSDbTest


from pms_dbmodel.models.e_operator import EArea
from pms_dbmodel.operator_operation.area_operation import AreaOperation
from pms_dbmodel.testoperatordata import TestOperatiorData


class AreaOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            EArea,
        )

    def testGetArea(self):
        a = AreaOperation.getArea(TestOperatiorData.area)
        self.assertIsInstance(a, EArea)
        assert a.name == TestOperatiorData.area

        b = AreaOperation.getArea(TestOperatiorData.area)
        assert a == b
