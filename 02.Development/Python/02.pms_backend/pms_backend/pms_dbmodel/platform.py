from enum import Enum
from pms_dbmodel.common_operation.category_operation import (
    CategoryOperation,
)
from pms_dbmodel.common import ArrayData
from pms_dbmodel.models.e_platform import EPlatform, EPlatformFamily, EGeneration
from pms_dbmodel.platform_operation.generation_operation import GenerationOperation
from pms_dbmodel.platform_operation.platform_operation import (
    PlatformOperation,
)
from pms_dbmodel.platform_operation.family_operation import PlatformFamilyOperation
from pms_dbmodel.operator_operation import logger
from pms_dbmodel.common import LOGTIME, logInfo
from pms_dbmodel.models.a_attribute import ACategory


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


class GenerationService:
    @classmethod
    def addGeneration(cls, id, name, external):
        GenerationOperation.addGerneration(id, name, external)

    @classmethod
    def getGeneration(cls, name) -> EGeneration:
        return GenerationOperation.getGeneration(name)


class PlatformService:
    @classmethod
    def addPlatformsWithGeneration(
        cls, id, gName, external_name=None, platform: list[PlatformData] = []
    ):
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
        GenerationOperation.addGerneration(id, gName, external_name)

        # 2. Get Category and Family
        categoryMap = CategoryOperation.getCategoryMap()
        fMap = cls._getFamilyMap(gName, platform)
        # 3. Add Platform
        cls._addPlatforms(platform, fMap, categoryMap)

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
    def _addPlatforms(cls, data: list[PlatformData], fMap, categoryMap):
        for d in data:
            family = fMap[d.getInfo(PlatformData.INFO.FAMILY)]

            cls._addPlatformWithFamilyAndCategory(d, family, categoryMap)

    @classmethod
    def _addPlatformWithFamilyAndCategory(
        cls,
        data: PlatformData,
        family: EPlatformFamily,
        categoryMap: dict[str, ACategory],
    ) -> EPlatform:
        category = categoryMap[data.getInfo(PlatformData.INFO.CATEGORY)]
        id = data.getInfo(PlatformData.INFO.ID)
        platform = data.getInfo(PlatformData.INFO.NAME)
        external = data.getInfo(PlatformData.INFO.EXTERNAL_NAME)

        return PlatformOperation.addPlatform(id, platform, external, family, category)

    @classmethod
    def getPlatform(cls, platform: str):
        result = PlatformOperation.getPlatform(platform)

        if result == None:
            raise Exception(" Can not find platform: " + platform)
        return result

    @classmethod
    def updatePlatformFamily(cls, fName, external):
        PlatformFamilyOperation.updatePlatformExternalName(fName, external)
