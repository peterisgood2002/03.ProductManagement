from pms_dbmodel.models.e_employee import EEmployee

from .base_test import PMSDbTest


class EmployeeTest(PMSDbTest):
    def setUp(self):
        super().setManaged(EEmployee)

    def test_insertEmployee(self):
        e = EEmployee(id=1, english_name="test")

        e.save()
        teste = EEmployee.objects.get(id=1)
        print(teste)
        self.assertNotEqual(teste, None)
