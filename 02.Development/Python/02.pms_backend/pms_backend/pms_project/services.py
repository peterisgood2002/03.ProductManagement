from excel_common.excel_operation import (
    ExcelParser,
    AbstractExcelService,
    SheetParserSercice,
)
from enum import Enum
from excel_common.item import Item
from pms_dbmodel.project import ProjectData, ProjectService
import openpyxl
from .util import *


class SHEETNAME(Enum):
    Home_Project = 0
    L1_Project = 1
    L2_Project = 2
    L3_Project = 3


class PROJECT(Enum):
    NAME = 0
    PLATFROM = 1
    Home = 2
    ODM = 3
    T2 = 4
    T1 = 5
    OEM = 6
    PRIORITY = 7
    TYPE = 8
    CPM = 9
    AM = 10


class ProjectParserService:
    @classmethod
    def collectIntoOneExcel(cls, homeFileName, l1FileName, l2FileName, l3FileName):
        """
            Collect from several location and output the excel which system can use
        Args:
            homeFileName (_type_): _description_
            l1FileName (_type_): _description_
            l2FileName (_type_): _description_
            l3FileName (_type_): _description_
        """

        home = openpyxl.load_workbook(homeFileName)
        l1 = openpyxl.load_workbook(l1FileName)
        l2 = openpyxl.load_workbook(l2FileName)
        l3 = openpyxl.load_workbook(l3FileName)
        result = openpyxl.Workbook()

        result.save(OUTPUT_FILE)

    @classmethod
    def getAllItem(cls, fileName) -> list[Item]:
        result = []

        excel = openpyxl.load_workbook(fileName)
        result += cls.parseHomeProject(fileName, excel)
        result += cls.parseL1Project(fileName, excel)
        result += cls.parseL2Project(fileName, excel)
        result += cls.parseL3Project(fileName, excel)
        return result

    @classmethod
    def parseHomeProject(cls, fileName, excel) -> list[Item]:
        sheet = excel[SHEETNAME.Home_Project.name]

        keyMap = {
            PROJECT.NAME: "Project Name",
            PROJECT.PLATFROM: "Chipset",
            PROJECT.Home: "Customer",
            PROJECT.PRIORITY: "Business Priority",
            PROJECT.TYPE: "Product Type",
        }

        return SheetParserSercice.parseSheet(fileName, sheet, keyMap, PROJECT)

    @classmethod
    def parseL1Project(cls, fileName, excel) -> list[Item]:
        sheet = excel[SHEETNAME.L1_Project.name]
        keyMap = {
            PROJECT.NAME: "Project Name",
            PROJECT.PLATFROM: "Chipset",
            PROJECT.OEM: "OEM",
            PROJECT.PRIORITY: "Business Priority",
            PROJECT.TYPE: "Product Type",
        }
        return SheetParserSercice.parseSheet(fileName, sheet, keyMap, PROJECT)

    @classmethod
    def parseL2Project(cls, fileName, excel) -> list[Item]:
        sheet = excel[SHEETNAME.L2_Project.name]
        keyMap = {
            PROJECT.NAME: "Project Name",
            PROJECT.PLATFROM: "Chipset",
            PROJECT.OEM: "OEM/Brand",
            PROJECT.ODM: "ODM",
            PROJECT.PRIORITY: "Business Priority",
            PROJECT.TYPE: "Product Type",
        }
        return SheetParserSercice.parseSheet(fileName, sheet, keyMap, PROJECT)

    @classmethod
    def parseL3Project(cls, fileName, excel) -> list[Item]:
        sheet = excel[SHEETNAME.L3_Project.name]
        keyMap = {
            PROJECT.NAME: "Project name",
            PROJECT.PLATFROM: "IC",
            PROJECT.OEM: "OEM",
            PROJECT.T1: "Tier-1",
            PROJECT.T2: "客戶",
            PROJECT.PRIORITY: "Business Priority",
            PROJECT.TYPE: "Product Type",
        }
        return SheetParserSercice.parseSheet(fileName, sheet, keyMap, PROJECT)


class ProjectService(AbstractExcelService):
    @classmethod
    def parse(cls, fileName):
        # 1. parsing excel to items
        # 2. Examine there are some customers or platforms does not exit in database
        # 3. sort out all items into ProjectData
        # 4. add or update project
        pass
