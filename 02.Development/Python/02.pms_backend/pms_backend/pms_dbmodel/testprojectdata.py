from pms_dbmodel.testplatformdata import TestPlatformData
from pms_dbmodel.project import CustomerData, ProjectData
from pms_dbmodel.models.e_customers import ECustomer


class TestCustomerData:
    cData = ["Customer1", "Customer2", "Customer3"]
    customer = [
        CustomerData(["CN", cData[0]]),
        CustomerData(["EU", cData[1]]),
        CustomerData(["JP", cData[2]]),
    ]


class CheckCustomerData:
    @staticmethod
    def checkCustomer(customer, area, name):
        assert isinstance(customer, ECustomer) == True
        assert customer.name == name
        assert int(customer.id / 100) == customer.area.id
        assert customer.area.name == area


class TestProjectData:
    project = [
        ProjectData(
            [TestPlatformData.pdata[0], "Project1", TestCustomerData.customer[0]]
        ),
        ProjectData(
            [TestPlatformData.pdata[0], "Project2", TestCustomerData.customer[1]]
        ),
    ]
