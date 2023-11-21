from enum import Enum
from pms_dbmodel.common import ArrayData
from pms_dbmodel.customer import CustomerService
from pms_dbmodel.platform import PlatformData, PlatformService
from pms_dbmodel.project_operation.project_operation import ProjectOperation
from pms_dbmodel.common_operation.category_operation import CategoryOperation
from pms_dbmodel.models.e_project import EProject


class CustomerData(ArrayData):
    class INFO(Enum):
        AREA = 0
        CUSTOMER = 1
        RELATIONSHIP = 2

    def getInfoLength(self):
        return len(CustomerData.INFO)


class ProjectData(ArrayData):
    class INFO(Enum):
        MAIN_PLATFROM = 0
        PROJCT_NAME = 1
        MAIN_CUSTOMER = 2

    def __init__(self, data=None):
        super().__init__(data)

        self._othercustomers = []
        self._otherplatforms = []

    def getInfoLength(self):
        return len(ProjectData.INFO)

    def addCustomer(self, customer: CustomerData):
        if customer not in self._othercustomers:
            self._othercustomers.append(customer)

    def addOtherPlatform(self, platform: PlatformData):
        if platform not in self._otherplatforms:
            self._otherplatforms.append(platform)

    def getAllCustomers(self) -> list[CustomerData]:
        result = []
        result.append(self.getInfo(ProjectData.INFO.MAIN_CUSTOMER))

        for c in self._othercustomers:
            result.append(c)

        return result

    def getAllPlatform(self) -> list[str]:
        result = []
        result.append(self.getInfo(ProjectData.INFO.MAIN_PLATFROM))

        for p in self._otherplatforms:
            result.append(p)

        return result

    def getMainCustomer(self) -> CustomerData:
        return self.getInfo(ProjectData.INFO.MAIN_CUSTOMER)

    def getMainPlatform(self) -> str:
        return self.getInfo(ProjectData.INFO.MAIN_PLATFROM)


class ProjectService:
    @classmethod
    def addProject(cls, project: ProjectData):
        # 1. Create project
        pName = project.getInfo(ProjectData.INFO.PROJCT_NAME)
        p = ProjectOperation.addProject(pName)
        # 2. Add Customer Relationship
        cls._addProjectCustomer(p, project.getAllCustomers())
        # 3. Add Platform Relationship
        cls._addProjectPlatform(p, project.getAllPlatform())

    @classmethod
    def _addProjectCustomer(cls, project: EProject, customers: list[CustomerData]):
        cMap = CategoryOperation.getCategoryMap()

        for customer in customers:
            area = customer.getInfo(CustomerData.INFO.AREA)
            cName = customer.getInfo(CustomerData.INFO.CUSTOMER)

            c = CustomerService.getOrAddCustomer(area, cName)
            relationship = customer.getInfo(CustomerData.INFO.RELATIONSHIP)

            ProjectOperation.addCustomerRelationshipWithObjects(
                project, c, cMap.get(relationship)
            )

    @classmethod
    def _addProjectPlatform(cls, project: EProject, platforms: list[str]):
        for platform in platforms:
            p = PlatformService.getPlatform(platform)

            ProjectOperation.addPlatformRelationshipWithObject(project, p)

    @classmethod
    def getCustomerRelationship(cls, projectName) -> list:
        return ProjectOperation.getCustomerRelationships(projectName)

    @classmethod
    def getPlatformRelationship(cls, projectName) -> list:
        return ProjectOperation.getPlatformRelationships(projectName)
