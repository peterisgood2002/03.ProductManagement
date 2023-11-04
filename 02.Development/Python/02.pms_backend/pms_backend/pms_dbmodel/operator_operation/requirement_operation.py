from .version_operation import VersionOperation
from pms_dbmodel.common import setDateAndSave, LOGTIME, logInfo
from pms_dbmodel.operator_operation import logger
from pms_dbmodel.models.e_operator import EComplianceVersion
from pms_dbmodel.models.a_attribute import APriority
from pms_dbmodel.models.e_operator_requirement import (
    EDocStructure,
    EDeviceRequirementDesc,
    EDeviceRequirement,
)


class RequirementOperation:
    @classmethod
    def addDeviceRequirementDesc(cls, title, name, desc="") -> EDeviceRequirementDesc:
        r = EDeviceRequirementDesc.objects.get_or_create(
            title=title, name=name, description=desc
        )
        setDateAndSave(r)

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
            "Operator = %s, Version = %s, ID = %s, Title = %s",
            operator,
            version_no,
            id,
            title,
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
    ) -> list:
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
    ) -> EDeviceRequirement:
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
        setDateAndSave(result)
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
    ):
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
    def getDeviceRequirementMapBasedOnTagId(cls, operator, version_no):
        rList = cls.getDeviceRequirementList(operator, version_no)

        result = {}

        for r in rList:
            key = r.tag_id
            result[key] = r

        return result

    @classmethod
    def getDeviceRequirement(cls, operator, version_no, id):
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
