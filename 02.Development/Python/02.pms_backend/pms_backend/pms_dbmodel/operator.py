from enum import Enum
from pms_dbmodel.operator_operation import logger
from pms_dbmodel.common import LOGTIME, logInfo
from pms_dbmodel.operator_operation.version_operation import VersionOperation
from pms_dbmodel.operator_operation.requirement_operation import (
    RequirementOperation,
    PriorityOperation,
)
from pms_dbmodel.operator_operation.doc_operation import DocOperation, StructureCategory
from pms_dbmodel.models.e_operator_requirement import (
    EDocStructure,
    EDocStructureCategory,
)


class OperatorRequirement:
    class INFO(Enum):
        VERSION = 0
        ChapterId = 1
        Chapter = 2
        SectionId = 3
        Section = 4
        TAG = 5
        TITLE = 6
        NAME = 7
        DESC = 8
        PRIORITY = 9

    def __init__(self, requirement=None):
        if len(requirement) <= len(OperatorRequirement.INFO):
            self._requirement = []
            for r in requirement:
                self._requirement.append(r)

            remaining = len(OperatorRequirement.INFO) - len(requirement)
            for i in range(remaining):
                self._requirement.append(None)

    def getInfo(self, info: INFO):
        return self._requirement[info.value]


class OperatorService:
    @classmethod
    def addOperatorRequirements(
        cls, area, operator, version_no, requirements: list[OperatorRequirement]
    ):
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addOperatorRequirements.__name__,
            "Operator = %s, Version = %s, Size = %s",
            operator,
            version_no,
            len(requirements),
        )

        # 1. Insert Version
        version = VersionOperation.getOrAddVersion(area, operator, version_no)
        # 2. Create a Map and insert doc structure
        structure = OperatorService.createDocStructureMap(version, requirements)
        # 3. Insert Device Requirement
        OperatorService.createDeviceRequirement(version, requirements, structure)

    @staticmethod
    def createDocStructureMap(
        version, data: list[OperatorRequirement]
    ) -> dict[str, EDocStructure]:
        result = {}  # <id, DocStructure>
        catMap = DocOperation.getDocStructureCategoryMap()

        for d in data:
            # if ChapterId does not exist in the dictionary, this data is Chapter. However if ChapterId exist in the dictionary, this means it inserted previously and can not be Chapter
            parent = OperatorService._createDocStructureMap(
                version,
                d,
                OperatorRequirement.INFO.ChapterId,
                OperatorRequirement.INFO.Chapter,
                None,
                catMap,
                result,
            )
            OperatorService._createDocStructureMap(
                version,
                d,
                OperatorRequirement.INFO.SectionId,
                OperatorRequirement.INFO.Section,
                parent,
                catMap,
                result,
            )

        return result

    @staticmethod
    def _createDocStructureMap(
        version,
        data: OperatorRequirement,
        idLocation: OperatorRequirement.INFO,
        titleLocation: OperatorRequirement.INFO,
        parent: EDocStructure,
        catMap: dict[str, EDocStructureCategory],
        result: dict,
    ) -> EDocStructure:
        id = data.getInfo(idLocation)
        title = data.getInfo(titleLocation)

        category = catMap[StructureCategory.Section.name]
        if parent == None:
            if result.get(id) == None:
                category = catMap[StructureCategory.Chapter.name]
            else:
                parent = result[id]

        [r, succeed] = DocOperation.addDocStructureWithVersion(
            version, category, id, title, parent
        )

        if succeed:
            result[id] = r

        return r

    @staticmethod
    def createDeviceRequirement(
        version,
        requirements: list[OperatorRequirement],
        strcture: dict[str, EDocStructure],
    ):
        pMap = PriorityOperation.getPriorityMap()

        for r in requirements:
            section = r.getInfo(OperatorRequirement.INFO.SectionId)
            tag = r.getInfo(OperatorRequirement.INFO.TAG)
            title = r.getInfo(OperatorRequirement.INFO.TITLE)
            name = r.getInfo(OperatorRequirement.INFO.NAME)
            desc = r.getInfo(OperatorRequirement.INFO.DESC)
            priority = r.getInfo(OperatorRequirement.INFO.PRIORITY)

            if priority != None and pMap.get(priority) == None:
                [p, succeed] = PriorityOperation.addPriority(priority)
                pMap[priority] = p

            RequirementOperation.addDeviceRequirementWithVersion(
                version, strcture[section], tag, title, name, desc, pMap.get(priority)
            )