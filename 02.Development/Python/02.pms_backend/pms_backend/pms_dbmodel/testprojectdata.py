from pms_dbmodel.testplatformdata import TestPlatformData
from pms_dbmodel.project import CustomerData, ProjectData
from pms_dbmodel.models.e_customers import ECustomer
from pms_dbmodel.models.e_project import EProject, RProjectCustomer
from pms_dbmodel.project_operation.customer_operation import CustomerCategory
from pms_dbmodel.models.r_project_platform import RProjectPlatform


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

    @staticmethod
    def getProject1() -> ProjectData:
        result = TestProjectData.project[0]
        # add another customer
        result.addCustomer(
            TestCustomerData.customer[1].getInfo(CustomerData.INFO.AREA),
            TestCustomerData.customer[1].getInfo(CustomerData.INFO.CUSTOMER),
            CustomerCategory.T1.name,
        )

        result.addCustomer(
            TestCustomerData.customer[2].getInfo(CustomerData.INFO.AREA),
            TestCustomerData.customer[2].getInfo(CustomerData.INFO.CUSTOMER),
            CustomerCategory.T2.name,
        )

        result.addOtherPlatform(TestPlatformData.pdata[1])
        return result


class CheckProjectData:
    @staticmethod
    def checkProject(data: EProject, id, name):
        assert isinstance(data, EProject)

        assert data.id == id
        assert data.name == name

    @staticmethod
    def checkCustomerRelation(data: RProjectCustomer, project, customer):
        assert isinstance(data, RProjectCustomer) == True
        assert data.customer.name == customer
        assert data.project.name == project

    @staticmethod
    def checkPlatformRelation(data: RProjectPlatform, project, platform):
        assert isinstance(data, RProjectPlatform) == True
        assert data.project.name == project
        assert data.platform.name == platform
