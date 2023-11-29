from django.db import models
import openpyxl
from enum import Enum
from excel_common.excel_operation import ExcelParser
from pms_dbmodel.platform import PlatformData
from pms_dbmodel.platform import PlatformService as P
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


# Create your models here.
class PlatformService:
    @classmethod
    def parse(cls, fileName):
        excel = openpyxl.load_workbook(fileName)
        generation = cls.parseGeneration(fileName, excel)

        # Get Map: <Family, Generation>
        fList = cls.parseFamily(fileName, excel)
        gMap = cls.getGenerationMapBasedOnFamily(fList)

        # Get Map: <Generation, list<PlatformData> >
        platforms = cls.parsePlatform(fileName, excel)

        dMap = cls.getMapAboutPlatformData(platforms, gMap)

        cls.addPlatforms(generation, dMap, P.addPlatformsWithGeneration)

        cls.updateFamilyExternal(fList, P.updatePlatformFamily)

    @classmethod
    def parseGeneration(cls, fileName, excel) -> list[Item]:
        sheet = excel[SHEETNAME.Generation.name]

        keyMap = {
            GENERATION.ID: "Id",
            GENERATION.NAME: "Name",
            GENERATION.EXTERNAL: "External_name",
        }

        parser = ExcelParser(keyRow=1, originalKeyMap=keyMap, keyInfo=GENERATION)

        parser.createMap(sheet)
        items = parser.parseExcel(fileName, 2, sheet)

        return items

    @classmethod
    def parseFamily(cls, fileName, excel) -> list[Item]:
        sheet = excel[SHEETNAME.Family.name]

        keyMap = {
            FAMILY.GENERATION: "Generation",
            FAMILY.NAME: "Name",
            FAMILY.EXTERNAL: "External_name",
        }
        parser = ExcelParser(keyRow=1, originalKeyMap=keyMap, keyInfo=FAMILY)

        parser.createMap(sheet)
        items = parser.parseExcel(fileName, 2, sheet)

        return items

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
    def addPlatforms(
        cls, generation: list[Item], dMap: dict[str, list[PlatformData]], func
    ):
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
                func(gId, gName, gExternal, data)

    @classmethod
    def updateFamilyExternal(cls, family: list[Item], func):
        for f in family:
            fName = f.getKey(FAMILY.NAME)
            fExternal = f.getKey(FAMILY.EXTERNAL)
            func(fName, fExternal)

    @classmethod
    def getGenerationMapBasedOneID(cls, data: list[Item]) -> dict[str, int]:
        result = {}

        for d in data:
            id = int(d.getKey(GENERATION.ID))
            name = d.getKey(GENERATION.NAME)
            result[name] = id

        return result
