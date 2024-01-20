from .base_test import PMSDbTest
from pms_dbmodel.models.e_milestone import EMilestone
from pms_dbmodel.models.a_attribute import ACategory
from pms_dbmodel.common_operation.category_operation import CategoryOperation
from pms_dbmodel.testmilestonedata import TestMilestoneData, CheckMilestoneData
from pms_dbmodel.milestone import MilestoneData
from pms_dbmodel.milestone_operation.milestone_operation import MilestoneOperation


class MilestoneOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            ACategory,
            EMilestone,
        )

    def _addCategory(self):
        i = 1
        for c in TestMilestoneData.category:
            CategoryOperation.addCategory(i, c)
            i += 1

    def _addMilestone(self, data: MilestoneData, catMap: dict, parent=None):
        category = data.getInfo(MilestoneData.INFO.CATEGORY)
        milestone = data.getInfo(MilestoneData.INFO.MILESTONE)
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

        CheckMilestoneData.checkMilestone(result, catMap[category], milestone, parent)
        return result

    def testAddMilstone(self):
        # 1. Add and Get Category
        self._addCategory()
        catMap = CategoryOperation.getCategoryMap()

        milestoneMap = {}
        for m in TestMilestoneData.milestone:
            milestone = m.getInfo(MilestoneData.INFO.MILESTONE)
            parent = m.getInfo(MilestoneData.INFO.PARENT_MILESTONE)
            result = None
            if parent == "":
                result = self._addMilestone(m, catMap)
            else:
                p = milestoneMap.get(parent)
                result = self._addMilestone(m, catMap, p)
            milestoneMap[milestone] = result

        result = MilestoneOperation.getMilestoneMap()

        assert len(result) == len(TestMilestoneData.milestone)
