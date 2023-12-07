from pms_dbmodel.project_operation.customer_operation import CustomerOperation
from pms_dbmodel.common_operation.area_operation import AreaOperation
from pms_dbmodel.models.e_customers import ECustomer


class CustomerService:
    @classmethod
    def getOrAddCustomer(cls, area: str, customer, alpha=False) -> ECustomer:
        result = cls.getCustomer(customer)

        if result == None:
            result = CustomerOperation.addCustomer(area, customer, alpha)

        return result

    @classmethod
    def getCustomers(cls, area: str = None) -> list[str]:
        if area != None:
            a = AreaOperation.getArea(area)
            return CustomerOperation.getCustomers(a)
        else:
            return CustomerOperation.getCustomers()

    @classmethod
    def getCustomer(cls, customer) -> ECustomer:
        return CustomerOperation.getCustomer(customer)
