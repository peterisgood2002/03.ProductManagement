from .base_test import PMSDbTest

from pms_dbmodel.project_operation.customer_operation import CustomerOperation
from pms_dbmodel.models.e_customers import ECustomer
from pms_dbmodel.models.e_employee import EEmployee
from pms_dbmodel.testprojectdata import TestCustomerData, CheckCustomerData
from pms_dbmodel.project import CustomerData


class CustomerOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            EEmployee,
            ECustomer,
        )

    def testAddCustomer(self):
        for c in TestCustomerData.customer:
            area = c.getInfo(CustomerData.INFO.AREA)
            customer = c.getInfo(CustomerData.INFO.CUSTOMER)
            CustomerOperation.addCustomer(area, customer)
            r = CustomerOperation.getCustomer(customer)
            CheckCustomerData.checkCustomer(r, area, customer)

        lResult = CustomerOperation.getCustomers()

        assert len(lResult) == len(TestCustomerData.customer)

        mResult = CustomerOperation.getCustomerAreaMap()
        assert len(mResult) == 3

    def testAddOrUpdateCustomer(self):
        id = 8888

        c = TestCustomerData.customer[0]
        area = c.getInfo(CustomerData.INFO.AREA)
        customer = c.getInfo(CustomerData.INFO.CUSTOMER)

        CustomerOperation.addOrUpdateCustomer(area, id, customer, True)

        result = CustomerOperation.getCustomerWithId(id)

        assert result != None
        assert result.update_date != None
