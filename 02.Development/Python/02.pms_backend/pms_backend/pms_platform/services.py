from django.db import models
import openpyxl
from enum import Enum
from excel_common.excel_operation import (
    ExcelParser,
    AbstractExcelService,
    SheetParserSercice,
)
from pms_dbmodel.platform import PlatformData
from pms_dbmodel.platform import GenerationService, PlatformService as P, FamilyService
from excel_common.item import Item


class SHEETNAME(Enum):
    Generation = 0
    Family = 1
    Platform = 2


class GENERATION(Enum):
    ID = 0
    NAME = 1
    EXTERNAL = 2


class FAMILY(Enum):
    GENERATION = 0
    NAME = 1
    EXTERNAL = 2


class PLATFORM(Enum):
    ID = 0
    NAME = 1
    EXTERNAL = 2
    FAMILY = 3
    CATEGORY = 4


class PlatformParserService:
    @classmethod
    def parseGeneration(cls, fileName, excel) -> list[Item]:
        sheet = excel[SHEETNAME.Generation.name]

        keyMap = {
            GENERATION.ID: "Id",
            GENERATION.NAME: "Name",
            GENERATION.EXTERNAL: "External_name",
        }

        return SheetParserSercice.parseSheet(fileName, sheet, keyMap, GENERATION)

    @classmethod
    def parseFamily(cls, fileName, excel) -> list[Item]:
        sheet = excel[SHEETNAME.Family.name]

        keyMap = {
            FAMILY.GENERATION: "Generation",
            FAMILY.NAME: "Name",
            FAMILY.EXTERNAL: "External_name",
        }

        return SheetParserSercice.parseSheet(fileName, sheet, keyMap, FAMILY)

    @classmethod
    def getGenerationMapBasedOnFamily(cls, family: list[Item]) -> dict[str, str]:
        result = {}

        for f in family:
            fName = f.getKey(FAMILY.NAME)
            gName = f.getKey(FAMILY.GENERATION)

            result[fName] = gName
        return result

    @classmethod
    def parsePlatform(cls, fileName, excel) -> list[Item]:
        sheet = excel[SHEETNAME.Platform.name]

        keyMap = {
            PLATFORM.ID: "Id",
            PLATFORM.NAME: "Name",
            PLATFORM.EXTERNAL: "External_name",
            PLATFORM.FAMILY: "Family",
            PLATFORM.CATEGORY: "Category",
        }
        parser = ExcelParser(keyRow=1, originalKeyMap=keyMap, keyInfo=PLATFORM)

        parser.createMap(sheet)
        items = parser.parseExcel(fileName, 2, sheet)

        return items

    @classmethod
    def getMapAboutPlatformData(
        cls, platforms: list[Item], gMap: dict[str, str]
    ) -> dict[str, list[PlatformData]]:
        result = {}

        for platform in platforms:
            id = int(platform.getKey(PLATFORM.ID))  # note that id should be an integer
            name = platform.getKey(PLATFORM.NAME)
            family = platform.getKey(PLATFORM.FAMILY)
            generation = gMap.get(family)
            external = platform.getKey(PLATFORM.EXTERNAL)
            category = platform.getKey(PLATFORM.CATEGORY)

            p = PlatformData([id, generation, family, name, external, category])

            r = result.get(generation, list())

            if len(r) == 0:
                result[generation] = r
            r.append(p)

        return result

    @classmethod
    def getGenerationMapBasedOneID(cls, data: list[Item]) -> dict[str, int]:
        result = {}

        for d in data:
            id = int(d.getKey(GENERATION.ID))
            name = d.getKey(GENERATION.NAME)
            result[name] = id

        return result


# Create your models here.
class PlatformService(AbstractExcelService):
    """
    BEGIN INTEGRATION TEST
    """

    @classmethod
    def parse(cls, fileName):
        excel = openpyxl.load_workbook(fileName)
        generation = PlatformParserService.parseGeneration(fileName, excel)

        PlatformService.addGeneration(generation)
        # Get Map: <Family, Generation>
        fList = PlatformParserService.parseFamily(fileName, excel)
        PlatformService.addFamily(fList)
        gMap = PlatformParserService.getGenerationMapBasedOnFamily(fList)

        # Get Map: <Generation, list<PlatformData> >
        platforms = PlatformParserService.parsePlatform(fileName, excel)

        dMap = PlatformParserService.getMapAboutPlatformData(platforms, gMap)

        PlatformService.addPlatforms(generation, dMap)

    @staticmethod
    def addGeneration(data: list[Item]):
        for g in data:
            gId = g.getKey(GENERATION.ID)
            gName = g.getKey(GENERATION.NAME)
            external = g.getKey(GENERATION.EXTERNAL)

            GenerationService.addGeneration(gId, gName, external)

    @staticmethod
    def addFamily(data: list[Item]):
        for f in data:
            gName = f.getKey(FAMILY.GENERATION)
            fName = f.getKey(FAMILY.NAME)
            fExternal = f.getKey(FAMILY.EXTERNAL)
            FamilyService.addPlatformFamilty(gName, fName, fExternal)

    @staticmethod
    def addPlatforms(generation: list[Item], dMap: dict[str, list[PlatformData]]):
        """

        We should call it normally but We adopt function call to implement addPlatforms feature due to Unit Test
        If we do not implement it in this way, we have to add Django Models dependency in this pms_platform project

        Args:
            generation (list[Item]): _description_
            dMap (dict[str, list[PlatformData]]): _description_
            func (_type_): _description_
        """
        for g in generation:
            gId = int(g.getKey(GENERATION.ID))
            gName = g.getKey(GENERATION.NAME)
            gExternal = g.getKey(GENERATION.EXTERNAL)
            data = dMap.get(gName)
            if data != None:
                P.addPlatformsWithGeneration(gId, gName, gExternal, data)

    """
    END INTEGRATION TEST
    """
