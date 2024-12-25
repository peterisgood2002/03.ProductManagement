from pms_dbmodel.common import *
from pms_dbmodel.milestone_operation import logger
from pms_dbmodel.models.a_attribute import ACategory
from pms_dbmodel.models.e_milestone import EMilestone
from pms_dbmodel.common_operation.common_operation import CommonOperation


class MilestoneOperation:
    @classmethod
    def addMilestone(
        cls,
        category: ACategory,
        milestone,
        deliverable,
        est_baseline: ACategory,
        estimated,
        parent: EMilestone = None,
    ) -> EMilestone:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addMilestone.__name__,
            "CATEGORY = %s, MILESTONE = %s, Deliverable = %s, ESTIMATED_BASELINE = %s, ESTIMATED = %f, PARENT_MILESTONE = %s",
            category.category_name,
            milestone,
            deliverable,
            "" if est_baseline == None else est_baseline.category_name,
            0 if estimated == None else estimated,
            "" if parent == None else parent.milestone_name,
        )
        """
          We provide the example in the database
          || id || milestone || parent ||
           | 10  |   M1       |
           | 11  |   M2       |
           | 12  |   M3       |
           | 10.1 |   M1A      |  10
           | 10.2 |   M1B      |  10
           | 11.1 |   M2A      |  11
           | 11.2 |   M2B      |  11
           | 10.11|   M1AA      | 10.1
          

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        if category == None:
            raise Exception("We do not have this category:" + category.category_name)

        milstones = EMilestone.objects.filter(
            category=category, parent_milestone=parent
        ).order_by("-id")

        result = None
        for m in milstones:
            if m.milestone_name == milestone:
                result = m

        if result == None:
            idx = (category.id * 10) if parent == None else (parent.id * 10 + 1)
            index = CommonOperation.getIntegerIndex(idx, milstones)

            r = EMilestone.objects.get_or_create(id=index, category=category)
            r[0].milestone_name = milestone
            r[0].deliverable = deliverable
            r[0].estimated_baseline = est_baseline
            r[0].estimated = estimated
            r[0].parent_milestone = parent
            CommonOperation.setDateAndSave(r)
            result = r[0]

        logInfo(
            logger,
            LOGTIME.END,
            cls.addMilestone.__name__,
            "[END] Result = %d",
            result.id,
        )
        return result

    @classmethod
    def getMilestoneMap(cls, category: str = None) -> dict[str, EMilestone]:
        result = {}

        for m in EMilestone.objects.all():
            if category == None:
                result[m.milestone_name] = m
            elif m.category.category_name == category:
                result[m.milestone_name] = m

        return result
