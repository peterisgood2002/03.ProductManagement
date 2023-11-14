from pms_dbmodel.common import setDateAndSave, LOGTIME, logInfo
from pms_dbmodel.models.e_operator import EComplianceVersion
from pms_dbmodel.models.e_operator_requirement import (
    EDocStructure,
    EDocStructureCategory,
)
from pms_dbmodel.operator_operation import logger
from .version_operation import VersionOperation
from enum import Enum


class StructureCategory(Enum):
    Document = 0
    Chapter = 1
    Section = 2


class DocOperation:
    @classmethod
    def addDocStructureCategory(cls, category) -> EDocStructureCategory:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addDocStructureCategory.__name__,
            "Category = %s",
            category,
        )
        r = EDocStructureCategory.objects.get_or_create(name=category)

        setDateAndSave(r)

        return r[0]

    @classmethod
    def getDocStructureCategory(cls, category) -> EDocStructureCategory:
        r = EDocStructureCategory.objects.filter(name=category)

        if len(r) == 0:
            return cls.addDocStructureCategory(category)

        return r[0]

    @classmethod
    def getDocStructureCategoryMap(cls) -> dict[str, EDocStructureCategory]:
        result = {}
        for d in EDocStructureCategory.objects.all():
            result[d.name] = d

        return result

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
    ) -> tuple[EDocStructure, bool]:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addDocStructure.__name__,
            "Area = %s, Operator = %s, Version = %s, Id = %s",
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
    ) -> tuple[EDocStructure, bool]:
        r = EDocStructure.objects.get_or_create(
            operator=version.operator, version=version, doc_id=id, category=category
        )

        if r[1] == False:
            # We insert this data previously so we return it directly and do not change anything
            return r
        r[0].name = title
        if parent != None:
            r[0].parent_structure_id = parent.doc_id
        setDateAndSave(r)

        return r

    @classmethod
    def getDocStructure(cls, operator, version, id):
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.getDocStructure.__name__,
            "[BEGIN], Operator = %s, Version = %s, Id = %s",
            operator,
            version,
            id,
        )
        result = EDocStructure.objects.filter(
            operator__name=operator, version=version, doc_id=id
        )
        if len(result) == 0:
            return None

        return result[0]
