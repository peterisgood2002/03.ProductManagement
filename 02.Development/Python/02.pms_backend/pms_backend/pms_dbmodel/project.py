from enum import Enum
from pms_dbmodel.common import ArrayData


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

    def __init__(self, requirement=None):
        super().__init__(requirement)

        self._othercustomers = []
        self._otherplatforms = []

    def getInfoLength(self):
        return len(ProjectData.INFO)

    def addCustomer(self, area, customer, relationship):
        self._othercustomers.append(CustomerData([area, customer, relationship]))

    def addOtherPlatform(self, platform):
        self._otherplatforms.append(platform)


class ProjectService:
    @classmethod
    def addProject(project: ProjectData):
        customer = project
