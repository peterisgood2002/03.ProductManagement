from enum import Enum
from pms_dbmodel.common_operation.category_operation import (
    CategoryOperation,
)
from pms_dbmodel.common import ArrayData
from pms_dbmodel.models.e_platform import EPlatform, EPlatformFamily
from pms_dbmodel.platform_operation.generation_operation import GenerationOperation
from pms_dbmodel.platform_operation.platform_operation import (
    PlatformOperation,
)
from pms_dbmodel.platform_operation.family_operation import PlatformFamilyOperation
from pms_dbmodel.operator_operation import logger
from pms_dbmodel.common import LOGTIME, logInfo


class PlatformData(ArrayData):
    class INFO(Enum):
        ID = 0
        GENERATION = 1
        FAMILY = 2
        NAME = 3
        EXTERNAL_NAME = 4
        CATEGORY = 5

    def getInfoLength(self):
        return len(PlatformData.INFO)


class PlatformService:
    @classmethod
    def addPlatformsWithGeneration(cls, id, gName, platform: list[PlatformData]):
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addPlatformsWithGeneration.__name__,
            "GenerationId = %d, Generation = %s, size = %d",
            id,
            gName,
            len(platform),
        )

        # 1. Get Generation
        generation = GenerationOperation.addGerneration(id, gName)

        # 2. Get Category and Family
        categoryMap = CategoryOperation.getCategoryMap()
        fMap = cls._getFamilyMap(gName, platform)
        # 3. Add Platform
        cls._addPlatform(platform, categoryMap, fMap)

    @classmethod
    def _getFamilyMap(
        cls, gName, data: list[PlatformData]
    ) -> dict[str, EPlatformFamily]:
        family = set()
        for d in data:
            f = d.getInfo(PlatformData.INFO.FAMILY)
            family.add(f)

        result = PlatformFamilyOperation.getFamilyMapBasedOnGen(gName)

        for f in family:
            if result.get(f) == None:
                d = PlatformFamilyOperation.addPlatformFamily(gName, f)
                result[f] = d
        return result

    @classmethod
    def _addPlatform(cls, data: list[PlatformData], categoryMap, fMap):
        for d in data:
            family = fMap[d.getInfo(PlatformData.INFO.FAMILY)]
            category = categoryMap[d.getInfo(PlatformData.INFO.CATEGORY)]

            id = d.getInfo(PlatformData.INFO.ID)
            platform = d.getInfo(PlatformData.INFO.NAME)
            external = d.getInfo(PlatformData.INFO.EXTERNAL_NAME)
            PlatformOperation.addPlatform(id, platform, external, family, category)
