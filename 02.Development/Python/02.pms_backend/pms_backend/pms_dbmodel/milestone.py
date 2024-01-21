from enum import Enum
from pms_dbmodel.common import ArrayData
from pms_dbmodel.milestone_operation.milestone_operation import MilestoneOperation
from pms_dbmodel.common_operation.category_operation import CategoryOperation
from pms_dbmodel.milestone_operation import logger
from pms_dbmodel.common import LOGTIME, logError
import time


class MilestoneData(ArrayData):
    class INFO(Enum):
        CATEGORY = 0
        MILESTONE = 1
        PARENT_MILESTONE = 2
        DELIVERABLE = 3
        ESTIMATED_BASELINE = 4
        ESTIMATED = 5

    def getInfoLength(self):
        return len(MilestoneData.INFO)


class MilestoneService:
    @classmethod
    def addMilstones(cls, data: list[MilestoneData]):
        # 1. Prepare data
        catMap = CategoryOperation.getCategoryMap()
        milestoneMap = cls._getMapBasedOnCategory(data)

        # 2. Add Milestone
        for category in milestoneMap:
            cls._addMilstones(milestoneMap[category], catMap)

    @classmethod
    def _getMapBasedOnCategory(cls, data: list[MilestoneData]) -> dict[str, list]:
        result = {}

        for d in data:
            category = d.getInfo(MilestoneData.INFO.CATEGORY)
            cList: list = result.get(category, [])
            cList.append(d)
            result[category] = cList

        return result

    @classmethod
    def _addMilstones(cls, data: list[MilestoneData], catMap):
        result = cls._addMilstonesWithoutParent(data, catMap)

        begin = time.time()
        time.sleep(1)
        end = time.time()
        print(end - begin)

        while len(result) != len(data):
            end = time.time()

            if end - begin > 300:
                cls._showNotProcessing(data, result)
                raise Exception("These data are processing too long")

            cls._addMilestonesWithParent(data, catMap, result)

        return result

    @classmethod
    def _addMilstonesWithoutParent(cls, data: list[MilestoneData], catMap) -> dict:
        result = {}
        for d in data:
            milestone = d.getInfo(MilestoneData.INFO.MILESTONE)
            parent = d.getInfo(MilestoneData.INFO.PARENT_MILESTONE)
            if parent == None or parent == "":
                r = cls._addMilestone(milestone, d, catMap)
                result[milestone] = r

        return result

    @classmethod
    def _addMilestonesWithParent(cls, data: list[MilestoneData], catMap, result: dict):
        for d in data:
            milestone = d.getInfo(MilestoneData.INFO.MILESTONE)
            if result.get(milestone) == None:
                parent = d.getInfo(MilestoneData.INFO.PARENT_MILESTONE)
                pMilestone = result.get(parent)
                if pMilestone != None:
                    r = cls._addMilestone(milestone, d, catMap, pMilestone)
                    result[milestone] = r

    @classmethod
    def _addMilestone(cls, milestone, data: MilestoneData, catMap: dict, parent=None):
        category = data.getInfo(MilestoneData.INFO.CATEGORY)
        deliverable = data.getInfo(MilestoneData.INFO.DELIVERABLE)
        estimated_baseline = data.getInfo(MilestoneData.INFO.ESTIMATED_BASELINE)
        estimated = data.getInfo(MilestoneData.INFO.ESTIMATED)

        result = MilestoneOperation.addMilestone(
            catMap.get(category),
            milestone,
            deliverable,
            catMap.get(estimated_baseline),
            estimated,
            parent,
        )
        return result

    @classmethod
    def _showNotProcessing(cls, data: list[MilestoneData], result: dict):
        for d in data:
            milestone = d.getInfo(MilestoneData.INFO.MILESTONE)
            if result.get(milestone) == None:
                logError(
                    logger,
                    LOGTIME.MIDDLE,
                    cls._addMilstones.__name__,
                    " Data = %s",
                    d.getData(),
                )

    @classmethod
    def getMilestonesMap(cls, category: str = None):
        return MilestoneOperation.getMilestoneMap(category)
