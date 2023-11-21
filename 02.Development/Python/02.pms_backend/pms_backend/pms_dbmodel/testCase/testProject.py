from .base_test import PMSDbTest
from pms_dbmodel.models.e_project import EProject, RProjectCustomer
from pms_dbmodel.models.a_attribute import ACategory
from pms_dbmodel.project_operation.project_operation import ProjectOperation
from pms_dbmodel.project_operation.customer_operation import CustomerOperation
from pms_dbmodel.testprojectdata import *
from pms_dbmodel.testplatformdata import TestPlatformData
from pms_dbmodel.project import CustomerData, ProjectData
from pms_dbmodel.common_operation.category_operation import CategoryOperation, Category
from pms_dbmodel.tests import Util
from pms_dbmodel.platform import PlatformService
from pms_dbmodel.models.r_project_platform import RProjectPlatform


class ProjectOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(ACategory, EProject, RProjectCustomer, RProjectPlatform)

    def testAddProject(self):
        for p in TestProjectData.project:
            name = p.getInfo(ProjectData.INFO.PROJCT_NAME)
            ProjectOperation.addProject(name)

            project = ProjectOperation.getProject(name)
            CheckProjectData.checkProject(project, name)

        projects = ProjectOperation.getProjects()

        assert len(projects) == len(TestProjectData.project)

    def testProjectRelationship(self):
        Util.addCustomerCategory()
        cMap = CategoryOperation.getCategoryMap()

        project = TestProjectData.getProject1()
        customer: CustomerData = project.getInfo(ProjectData.INFO.MAIN_CUSTOMER)

        p = ProjectOperation.addProject(project.getInfo(ProjectData.INFO.PROJCT_NAME))

        c = CustomerOperation.addCustomer(
            customer.getInfo(CustomerData.INFO.AREA),
            customer.getInfo(CustomerData.INFO.CUSTOMER),
        )

        [result, succeed] = ProjectOperation.addCustomerRelationship(
            project.getInfo(ProjectData.INFO.PROJCT_NAME),
            customer.getInfo(CustomerData.INFO.CUSTOMER),
            CustomerCategory.HOME.name,
            cMap,
        )

        rList = ProjectOperation.getCustomerRelationships(
            project.getInfo(ProjectData.INFO.PROJCT_NAME)
        )
        assert 1 == len(rList)
        CheckProjectData.checkCustomerRelation(
            rList[0],
            project.getInfo(ProjectData.INFO.PROJCT_NAME),
            customer.getInfo(CustomerData.INFO.CUSTOMER),
        )

        # Platform
        CategoryOperation.addCategory(Category.Platform.value, Category.Platform.name)
        CategoryOperation.addCategory(
            TestPlatformData.categoryId, TestPlatformData.category
        )
        PlatformService.addPlatformsWithGeneration(
            TestPlatformData.Gen1Id,
            TestPlatformData.Gen1Name,
            TestPlatformData.platform,
        )

        [result, succeed] = ProjectOperation.addPlatformRelationship(
            project.getInfo(ProjectData.INFO.PROJCT_NAME),
            project.getInfo(ProjectData.INFO.MAIN_PLATFROM),
        )

        rList = ProjectOperation.getPlatformRelationships(
            project.getInfo(ProjectData.INFO.PROJCT_NAME)
        )

        assert 1 == len(rList)
        CheckProjectData.checkPlatformRelation(
            rList[0],
            project.getInfo(ProjectData.INFO.PROJCT_NAME),
            project.getInfo(ProjectData.INFO.MAIN_PLATFROM),
        )
