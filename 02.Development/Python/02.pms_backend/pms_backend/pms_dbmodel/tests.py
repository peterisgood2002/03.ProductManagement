# Create your tests here.
from contextlib import contextmanager
from enum import Enum
from django.test import TestCase
from pms_dbmodel.common_operation.priority_operation import (
    PriorityOperation,
    PriorityCategory,
)


from pms_dbmodel.testCase.base_test import PMSDbTest
from pms_dbmodel.testoperatordata import TestOperatiorData
from pms_dbmodel.models.e_operator import EOperator
from pms_dbmodel.operator_operation.doc_operation import DocOperation, StructureCategory
from pms_dbmodel.operator import OperatorService
from pms_dbmodel.operator_operation.requirement_operation import RequirementOperation
from pms_dbmodel.operator_operation.version_operation import VersionOperation
from pms_dbmodel.models.e_platform import EPlatform

from pms_dbmodel.testplatformdata import TestPlatformData
from pms_dbmodel.platform import PlatformService
from pms_dbmodel.common_operation.category_operation import CategoryOperation, Category
from pms_dbmodel.project_operation.customer_operation import CustomerCategory
from pms_dbmodel.testprojectdata import TestProjectData
from pms_dbmodel.project import ProjectService, ProjectData
from django.db import models


class Util:
    @staticmethod
    def addDocCategories():
        for c, member in StructureCategory.__members__.items():
            category = DocOperation.addDocStructureCategory(c)
            assert category.name == c

    @staticmethod
    def addPriority():
        for c, member in PriorityCategory.__members__.items():
            [priority, succeed] = PriorityOperation.addPriority(c)
            assert priority.name == c

    @staticmethod
    def addCustomerCategory():
        parent = CategoryOperation.addCategory(
            Category.Customer.value, Category.Customer.name
        )

        for c, member in CustomerCategory.__members__.items():
            category = CategoryOperation.addCategoryWithParent(c, parent)

    @staticmethod
    def addPlatform():
        CategoryOperation.addCategory(Category.Platform.value, Category.Platform.name)
        CategoryOperation.addCategory(
            TestPlatformData.categoryId, TestPlatformData.category
        )
        PlatformService.addPlatformsWithGeneration(
            TestPlatformData.Gen1Id,
            TestPlatformData.Gen1Name,
            TestPlatformData.platform,
        )


class OperatorServiceTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            EOperator,
        )

    def testAddChapterAndSection(self):
        Util.addDocCategories()
        version = VersionOperation.getOrAddVersion(
            TestOperatiorData.area,
            TestOperatiorData.operator1,
            TestOperatiorData.version19,
        )
        result = OperatorService.createDocStructureMap(
            version, TestOperatiorData.requirement_19
        )

        for key, r in result.items():
            if key == "1" or key == "2":
                assert r.category.name == StructureCategory.Chapter.name
            else:
                assert r.category.name == StructureCategory.Section.name

    def testAddOperatorRequirement(self):
        Util.addDocCategories()
        OperatorService.addOperatorRequirements(
            TestOperatiorData.area,
            TestOperatiorData.operator1,
            TestOperatiorData.version19,
            TestOperatiorData.requirement_19,
        )

        result19 = RequirementOperation.getDeviceRequirementList(
            TestOperatiorData.operator1, TestOperatiorData.version19
        )

        assert len(result19) == len(TestOperatiorData.requirement_19)

        OperatorService.addNoChangedRequirements(
            TestOperatiorData.area,
            TestOperatiorData.operator1,
            TestOperatiorData.version22,
            TestOperatiorData.requirement_22_No,
        )

        result22 = RequirementOperation.getDeviceRequirementList(
            TestOperatiorData.operator1, TestOperatiorData.version22
        )

        assert len(result22) == len(TestOperatiorData.requirement_22_No)


class PlatformServiceTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            EPlatform,
        )

    def testAddPlatform(self):
        Util.addPlatform()


class ProjectServiceTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            EPlatform,
        )

    def testAddProject(self):
        project = TestProjectData.getProject1()
        Util.addPlatform()
        Util.addCustomerCategory()
        ProjectService.addProject(project)

        pName = project.getInfo(ProjectData.INFO.PROJCT_NAME)
        rList = ProjectService.getCustomerRelationship(pName)

        assert len(project.getAllCustomers()) == len(rList)

        rList = ProjectService.getPlatformRelationship(pName)
        assert len(project.getAllPlatform()) == len(rList)
