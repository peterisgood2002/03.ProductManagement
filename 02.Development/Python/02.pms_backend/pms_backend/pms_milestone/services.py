from excel_common.excel_operation import (
    ExcelParser,
    AbstractExcelService,
    SheetParserSercice,
)

from enum import Enum
from excel_common.item import Item
from pms_dbmodel.milestone import MilestoneData, MilestoneService as MS
import openpyxl


class SHEETNAME(Enum):
    Milestone = 0


class MILESTONE(Enum):
    CATEGORY = 0
    MILESTONE = 1
    PARENT_MILESTONE = 2
    DELIVERABLE = 3
    ESTIMATED_BASELINE = 4
    ESTIMATED = 5


class MilestoneParserService:
    @classmethod
    def parseMilestone(cls, fileName, excel) -> list[Item]:
        sheet = excel[SHEETNAME.Milestone.name]
        keyMap = {
            MILESTONE.CATEGORY: "Category",
            MILESTONE.MILESTONE: "Milestone",
            MILESTONE.PARENT_MILESTONE: "Parent_Milestone",
            MILESTONE.DELIVERABLE: "Deliverable",
            MILESTONE.ESTIMATED_BASELINE: "Estimated_Baseline",
            MILESTONE.ESTIMATED: "Estimated",
        }

        return SheetParserSercice.parseSheet(fileName, sheet, keyMap, MILESTONE)

    @classmethod
    def createMilestoneData(cls, data: list[Item]) -> list[MilestoneData]:
        result = []
        for d in data:
            category = d.getKey(MILESTONE.CATEGORY)
            milestone = d.getKey(MILESTONE.MILESTONE)
            parent = d.getKey(MILESTONE.PARENT_MILESTONE)
            deliverable = d.getKey(MILESTONE.DELIVERABLE)
            baseline = d.getKey(MILESTONE.ESTIMATED_BASELINE)
            estimated = d.getKey(MILESTONE.ESTIMATED)
            result.append(
                MilestoneData(
                    [category, milestone, parent, deliverable, baseline, estimated]
                )
            )
        return result


class MilestoneService(AbstractExcelService):
    @classmethod
    def parse(cls, fileName):
        excel = openpyxl.load_workbook(fileName)

        data = MilestoneParserService.parseMilestone(fileName, excel)

        result = MilestoneParserService.createMilestoneData(data)

        MS.addMilstones(result)
