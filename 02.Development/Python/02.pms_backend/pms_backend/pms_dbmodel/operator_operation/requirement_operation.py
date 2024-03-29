from .version_operation import VersionOperation
from pms_dbmodel.common import *
from pms_dbmodel.operator_operation import logger
from pms_dbmodel.models.e_operator import EComplianceVersion
from pms_dbmodel.models.a_attribute import APriority
from pms_dbmodel.models.e_operator_requirement import (
    EDocStructure,
    EDeviceRequirementDesc,
    EDeviceRequirement,
    ERequirementCategory,
    RDeviceRequirementCategory,
)
from enum import Enum
from pms_dbmodel.common_operation.common_operation import CommonOperation


class RequirementOperation:
    @classmethod
    def addDeviceRequirementDesc(
        cls, title, name, desc=""
    ) -> tuple[EDeviceRequirementDesc, bool]:
        r = EDeviceRequirementDesc.objects.get_or_create(
            title=title, name=name, description=desc
        )
        CommonOperation.setDateAndSave(r)

        return r

    @classmethod
    def getDeviceRequirementDesc(cls, id):
        logInfo(
            logger, LOGTIME.BEGIN, cls.getDeviceRequirementDesc.__name__, "ID = %s", id
        )

        result = EDeviceRequirementDesc.objects.filter(id=id)
        if len(result) == 0:
            return None

        return result[0]

    @classmethod
    def getDeviceRequirmentDecList(cls, title, name=None, desc=None):
        result = EDeviceRequirementDesc.objects.filter(
            title=title, name=name, description=desc
        )

        return result

    # BEGIN addNewDeviceRequirement
    @classmethod
    def addNewDeviceRequirement(
        cls,
        area,
        operator,
        version_no,
        docStucture: EDocStructure,
        id,
        title,
        name,
        description="",
        priority: APriority = None,
    ) -> list:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addNewDeviceRequirement.__name__,
            "Operator = %s, Version = %s, ID = %s, Title = %s, Name = %s, Desc = %s",
            operator,
            version_no,
            id,
            title,
            name,
            description,
        )
        version = VersionOperation.getOrAddVersion(area, operator, version_no)

        return cls.addDeviceRequirementWithVersion(
            version,
            docStucture,
            id,
            title,
            name,
            description=description,
            priority=priority,
        )

    @classmethod
    def addDeviceRequirementWithVersion(
        cls,
        version: EComplianceVersion,
        docStucture: EDocStructure,
        id,
        title,
        name,
        description="",
        priority: APriority = None,
    ) -> tuple[EDeviceRequirement, bool]:
        [descId, succeed] = cls.addDeviceRequirementDesc(title, name, description)

        return cls.createDeviceRequirementWithKeys(
            version, docStucture, descId, id, priority
        )

    @classmethod
    def createDeviceRequirementWithKeys(
        cls,
        version: EComplianceVersion,
        docStucture: EDocStructure,
        descId: EDeviceRequirementDesc,
        id,
        priority: APriority = None,
    ) -> tuple[EDeviceRequirement, bool]:
        result = EDeviceRequirement.objects.get_or_create(
            operator=version.operator,
            version=version,
            descId=descId,
        )

        if docStucture != None:
            result[0].structure_id = docStucture.doc_id

        result[0].tag_id = id

        if priority != None:
            result[0].priority = priority
        CommonOperation.setDateAndSave(result)
        return result

    # END addNewDeviceRequirement
    @classmethod
    def addNoChangeDeviceRequirement(
        cls,
        area,
        operator,
        version_no,
        docStucture: EDocStructure,
        id,
        idMap: dict,
        priority: APriority = None,
    ) -> tuple[EDeviceRequirement, bool]:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addNoChangeDeviceRequirement.__name__,
            "Operator = %s, Version = %s, ID = %s",
            operator,
            version_no,
            id,
        )
        version = VersionOperation.getOrAddVersion(area, operator, version_no)

        return cls.addNoChangeDeviceRequirementWithVersion(
            version, docStucture, id, idMap, priority
        )

    @classmethod
    def addNoChangeDeviceRequirementWithVersion(
        cls,
        version: EComplianceVersion,
        docStucture: EDocStructure,
        id,
        idMap: dict,
        priority: APriority = None,
    ) -> tuple[EDeviceRequirement, bool]:
        preReq = idMap.get(id)
        if preReq != None:
            descId = preReq.descId
            return cls.createDeviceRequirementWithKeys(
                version, docStucture, descId, id, priority
            )
        else:
            return [None, False]

    @classmethod
    def getDeviceRequirementList(cls, operator, version_no):
        rList = EDeviceRequirement.objects.filter(
            operator__name=operator, version__version_no=version_no
        )
        logInfo(
            logger,
            LOGTIME.END,
            cls.getDeviceRequirementList.__name__,
            "Operator = %s, Version = %s, size = %s",
            operator,
            version_no,
            len(rList),
        )
        return rList

    @classmethod
    def getDeviceRequirementMapBasedOnTagId(
        cls, operator, version_no
    ) -> dict[str, EDeviceRequirement]:
        """_summary_

        Args:
            operator (_type_): _description_
            version_no (_type_): _description_

        Returns:
            dict[str, EDeviceRequirement]: <tagId, EDeviceRequirement>
        """
        rList = cls.getDeviceRequirementList(operator, version_no)

        result = {}

        for r in rList:
            key = r.tag_id
            result[key] = r

        return result

    @classmethod
    def getDeviceRequirement(cls, operator, version_no, id) -> EDeviceRequirement:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.getDeviceRequirement.__name__,
            "Operator = %s, Version = %s, ID = %s",
            operator,
            version_no,
            id,
        )

        rList = EDeviceRequirement.objects.filter(
            operator__name=operator, version__version_no=version_no, tag_id=id
        )

        if len(rList) == 0:
            return None

        return rList[0]

    @classmethod
    def addCategory(cls, name) -> tuple[ERequirementCategory, bool]:
        result = ERequirementCategory.objects.get_or_create(name=name)

        CommonOperation.setDateAndSave(result)
        return result

    @classmethod
    def addCategoryWithTagId(cls, operator, version_no, id, category):
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addCategoryWithTagId.__name__,
            "Operator = %s, Version = %s, ID = %s, Category = %s",
            operator,
            version_no,
            id,
            category,
        )
        data = cls.getDeviceRequirement(operator, version_no, id)
        [category, succeed] = cls.addCategory(category)

        result = RDeviceRequirementCategory.objects.get_or_create(
            descId=data.descId,
            category=category,
        )

        CommonOperation.setDateAndSave(result)
        return result

    @classmethod
    def getCategories(cls, operator, version, id) -> list[str]:
        data = cls.getDeviceRequirement(operator, version, id)
        rList = RDeviceRequirementCategory.objects.filter(
            descId=data.descId,
        )

        result = []
        for l in rList:
            result.append(l.category.name)

        return result
