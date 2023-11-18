from pms_dbmodel.common import *
from pms_dbmodel.models.e_project import EProject, RProjectCustomer
from pms_dbmodel.models.r_project_platform import RProjectPlatform
from pms_dbmodel.models.e_customers import ECustomer
from pms_dbmodel.platform_operation import logger
from pms_dbmodel.models.a_attribute import ACategory
from .customer_operation import CustomerOperation
from pms_dbmodel.models.e_platform import EPlatform
from pms_dbmodel.common_operation.common_operation import CommonOperation
from pms_dbmodel.platform_operation.platform_operation import PlatformOperation
from pms_dbmodel.common_operation.common_operation import CommonOperation


class ProjectOperation:
    @classmethod
    def addProject(cls, id, name) -> EProject:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addProject.__name__,
            "Id = %s, Name = %s ",
            id,
            name,
        )

        result = EProject.objects.get_or_create(id=id)
        result[0].name = name
        CommonOperation.setDateAndSave(result)

        return result[0]

    @classmethod
    def getProject(cls, name) -> EProject:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.getProject.__name__,
            "Project = %s ",
            name,
        )

        return CommonOperation.searchWithName(name, EProject)

    @classmethod
    def getProjects(cls) -> list[str]:
        data = EProject.objects.all()
        result = []
        for d in data:
            result.append(d.name)

        logInfo(
            logger,
            LOGTIME.END,
            cls.getProjects.__name__,
            "Size = %d",
            len(result),
        )
        return result

    @classmethod
    def addCustomerRelationship(
        cls, project, customer, relationship, cMap
    ) -> tuple[RProjectCustomer, bool]:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addCustomerRelationship.__name__,
            "Project = %s, Customer = %s, CustomerLevel = %s",
            project,
            customer,
            relationship,
        )
        p = cls.getProject(project)
        c = CustomerOperation.getCustomer(customer)

        r = cMap[relationship]
        return cls._addCustomerRelationship(p, c, r)

    @classmethod
    def _addCustomerRelationship(
        cls, project: EProject, customer: ECustomer, relationship: ACategory
    ) -> tuple[RProjectCustomer, bool]:
        result = RProjectCustomer.objects.get_or_create(
            customer=customer, project=project, relationship=relationship
        )

        CommonOperation.setDateAndSave(result)

        return result

    @classmethod
    def addPlatformRelationship(
        cls, projectName, platformName
    ) -> tuple[RProjectPlatform, bool]:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addPlatformRelationship.__name__,
            "Project = %s, Platform = %s",
            projectName,
            platformName,
        )

        project = cls.getProject(projectName)
        platform = PlatformOperation.getPlatform(platformName)

        result = RProjectPlatform.objects.get_or_create(
            project=project, platform=platform
        )

        CommonOperation.setDateAndSave(result)

        return result
