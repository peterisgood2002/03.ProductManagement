from enum import Enum
from pms_dbmodel.common import ArrayData


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
