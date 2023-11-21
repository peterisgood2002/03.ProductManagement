from pms_dbmodel.project_operation.customer_operation import CustomerOperation
from pms_dbmodel.models.e_customers import ECustomer


class CustomerService:
    @classmethod
    def getOrAddCustomer(cls, area, customer) -> ECustomer:
        result = CustomerOperation.getCustomer(customer)

        if result == None:
            result = CustomerOperation.addCustomer(area, customer)

        return result

    @classmethod
    def getCustomers(cls, area=None) -> list[str]:
        return CustomerOperation.getCustomers()
