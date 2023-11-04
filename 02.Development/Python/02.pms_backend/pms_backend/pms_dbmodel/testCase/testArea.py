from .base_test import PMSDbTest
from .data import TestData

from pms_dbmodel.models.e_operator import EArea
from pms_dbmodel.operator_models import AreaOperation


class AreaOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            EArea,
        )

    def testGetArea(self):
        a = AreaOperation.getArea(TestData.area)
        self.assertIsInstance(a, EArea)
        assert a.name == TestData.area

        b = AreaOperation.getArea(TestData.area)
        assert a == b
