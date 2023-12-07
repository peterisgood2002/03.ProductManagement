from django.db import models
from pms_dbmodel.customer import CustomerService as c


# Create your models here.
class CustomerService:
    @staticmethod
    def addCustomer(area, name, id=None, alpha=False):
        customers = CustomerService.getCustomer(name)
        if name in customers:
            raise Exception("This customer is in the database, please update it.")
        else:
            c.getOrAddCustomer(area, name)

    @staticmethod
    def getCustomer(customer):
        return c.getCustomer(customer)

    @staticmethod
    def getCustomers(area=None) -> list[str]:
        return c.getCustomers(area)
