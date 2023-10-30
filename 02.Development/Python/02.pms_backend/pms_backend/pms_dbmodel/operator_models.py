from datetime import date
from django.db import models

from pms_dbmodel.models.e_operator import EComplianceVersion
from pms_dbmodel.models.e_operator import EOperator
from pms_dbmodel.models.e_operator import EArea
from pms_dbmodel.models.a_attribute import APriority
from pms_dbmodel.models.e_operator_requirement import (
    EDocStructureCategory,
    EDocStructure,
    EDeviceRequirementDesc,
    EDeviceRequirement,
)
import logging


class OperatorRequirement:
    def __init__(self, Id, title, description, chapterId, chapter, sectionId, section):
        self._id = Id
        self._title = title
        self._description = description
        self._chapterId = chapterId
        self._chapter = chapter
        self._sectionId = sectionId
        self._section = section

    def getChapterId(self):
        return self._chapterId

    def getSectionId(self):
        return self._sectionId


def _setDateAndSave(data):
    if data[1] == True:
        data[0].create_date = date.today()
        data[0].update_date = date.today()
    else:
        data[0].update_date = date.today()
    data[0].save()


logger = logging.getLogger("OperatorOperation")


class AreaOperation:
    @classmethod
    def getArea(cls, area) -> EArea:
        r = EArea.objects.get_or_create(name=area)
        _setDateAndSave(r)

        return r[0]


# Create your models here.
class OperatorOperation:
    @classmethod
    def addOperator(cls, area, operator) -> EOperator:
        logger.info("[getOperator][BEGIN] AREA = %s, Operator = %s", area, operator)
        a: EArea = AreaOperation.getArea(area)
        operators = EOperator.objects.filter(area=a).order_by("-id")

        result = None

        for o in operators:
            if o.name == operator:
                result = o

        if result == None:
            index = a.id * 100
            if len(operators) != 0:
                index = operators[0].id + 1
            r = EOperator.objects.get_or_create(id=index, name=operator, area=a)
            result = r[0]
        logger.info("[getOperator][END] Result = %d", result.id)
        return result

    @classmethod
    def getOperator(cls, operator) -> EOperator:
        logger.info("[getOperator][BEGIN] Operator = %s", operator)
        operator = EOperator.objects.filter(name=operator)

        if len(operator) == 0:
            return None
        return operator[0]


class VersionOperation:
    @classmethod
    def _addVersion(cls, area, operator, version):
        o = OperatorOperation.addOperator(area, operator)

        result = EComplianceVersion.objects.get_or_create(
            operator=o, version_no=version
        )
        _setDateAndSave(result)

        return result

    @classmethod
    def addVersion(cls, area, operator, version):
        v = cls._addVersion(area, operator, version)
        logger.info(
            "[addVersion][END] AREA = %s, Operator = %s, Version = %s, Insert/Update(True/False) = %s",
            area,
            operator,
            version,
            v[1],
        )

        return v

    @classmethod
    def getVersions(cls, area, operator):
        # 1. check whether this operator is the first one
        o = OperatorOperation.getOperator(operator)
        # 2. get the versions for this operator
        versions = EComplianceVersion.objects.filter(operator=o)

        r = []
        for v in versions:
            r.append(v.version_no)

        return r

    @classmethod
    def _getVersion(cls, area, operator, version):
        logger.info(
            "[getVersion][BEGIN] AREA = %s, Operator = %s, Version = %s",
            area,
            operator,
            version,
        )

        v = cls._addVersion(area, operator, version)

        return v[0]

    @classmethod
    def getVersion(cls, operator, version):
        logger.info(
            "[getVersion][BEGIN] Operator = %s, Version = %s", operator, version
        )
        version = EComplianceVersion.objects.filter(
            operator__name=operator, version_no=version
        )
        if len(version) == 0:
            return None

        return version[0]

    @classmethod
    def getOrAddVersion(cls, area, operator, version_no):
        version = VersionOperation.getVersion(operator, version_no)
        if version == None:
            [version, succeed] = VersionOperation.addVersion(area, operator, version_no)
        return version


class DocOperation:
    @classmethod
    def addDocStructureCategory(cls, category) -> EDocStructureCategory:
        logger.info("[addDocStructureCategory][BEGIN] Category = %s", category)
        r = EDocStructureCategory.objects.get_or_create(name=category)

        _setDateAndSave(r)

        return r[0]

    @classmethod
    def getDocStructureCategory(cls, category):
        r = EDocStructureCategory.objects.get_or_create(name=category)
        _setDateAndSave(r)

        return r[0]

    @classmethod
    def addDocStructure(
        cls,
        area,
        operator,
        version_no,
        category,
        id,
        title,
        parent: EDocStructure = None,
    ):
        logger.info(
            "[addDocStructure][BEGIN] Area = %s, Operator = %s, Version = %s, Id = %s",
            area,
            operator,
            version_no,
            id,
        )

        cate = cls.getDocStructureCategory(category)
        version = VersionOperation.getOrAddVersion(area, operator, version_no)
        return cls.addDocStructureWithVersion(version, cate, id, title, parent)

    @classmethod
    def addDocStructureWithVersion(
        cls,
        version: EComplianceVersion,
        category: EDocStructureCategory,
        id,
        title,
        parent: EDocStructure = None,
    ):
        r = EDocStructure.objects.get_or_create(
            operator=version.operator,
            version=version,
            category=category,
            id=id,
            name=title,
        )

        if parent != None:
            r[0].parent_structure = parent
        _setDateAndSave(r)

        return r

    @classmethod
    def getDocStructure(cls, operator, version, id):
        logger.info(
            "[getDocStructure][BEGIN], Operator = %s, Version = %s, Id = %s",
            operator,
            version,
            id,
        )
        result = EDocStructure.objects.filter(
            operator__name=operator, version=version, id=id
        )
        if len(result) == 0:
            return None

        return result[0]


class RequirementOperation:
    @classmethod
    def addDeviceRequirementDesc(cls, title, name, desc="") -> EDeviceRequirementDesc:
        r = EDeviceRequirementDesc.objects.get_or_create(
            title=title, name=name, description=desc
        )
        _setDateAndSave(r)

        return r

    @classmethod
    def getDeviceRequirementDesc(cls, id):
        logger.info("[getDeviceRequirementDesc][BEGIN],ID = %s", id)
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
        logger.info(
            "[addDeviceRequirement][BEGIN] Operator = %s, Version = %s, ID = %s, Title = %s",
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

        r = cls.addDeviceRequirementWithKeys(version, docStucture, descId)

        r[0].tag_id = id
        r[0].structure = docStucture
        if priority != None:
            r[0].priority = priority
        _setDateAndSave(r)

        return r

    @classmethod
    def addDeviceRequirementWithKeys(
        cls,
        version: EComplianceVersion,
        docStucture: EDocStructure,
        descId: EDeviceRequirementDesc,
    ) -> EDeviceRequirement:
        result = EDeviceRequirement.objects.get_or_create(
            operator=version.operator,
            version=version,
            structure=docStucture,
            descId=descId,
        )

        return result

    @classmethod
    def getDeviceRequirementList(cls, operator, version_no):
        rList = EDeviceRequirement.objects.filter(
            operator__name=operator, version__version_no=version_no
        )
        logger.info(
            "[getDeviceRequirementList][END] Operator = %s, Version = %s, size = %s",
            operator,
            version_no,
            len(rList),
        )
        return rList

    @classmethod
    def getDeviceRequirement(cls, operator, version_no, id):
        logger.info(
            "[getDeviceRequirement][BEGIN] Operator = %s, Version = %s, ID = %s",
            operator,
            version_no,
            id,
        )

        r = EDeviceRequirement.objects.filter(
            operator__name=operator, version__version_no=version_no, tag_id=id
        )
