from pms_dbmodel.milestone import MilestoneData
from pms_dbmodel.models.e_milestone import EMilestone
from pms_dbmodel.models.a_attribute import ACategory


class TestMilestoneData:
    category = ["Certification", "MONTH", "WEEK", "DAY", "Operator"]
    milestone = [
        MilestoneData([category[0], "MC111", "MC11", "TEST9", category[3], 1.6]),
        MilestoneData([category[0], "MC1", "", "TEST3", category[1], 1.0]),
        MilestoneData([category[0], "MC2", "", "TEST4", category[1], 1.1]),
        MilestoneData([category[0], "MC3", "", "TEST5", category[1], 1.2]),
        MilestoneData([category[0], "MC11", "MC1", "TEST6", category[2], 1.3]),
        MilestoneData([category[0], "MC12", "MC1", "TEST7", category[2], 1.4]),
        MilestoneData([category[0], "MC13", "MC1", "TEST8", category[2], 1.5]),
        MilestoneData([category[0], "MC22", "MC2", "TEST4", category[2], 1.1]),
        MilestoneData([category[4], "MO1", "", "TEST4", category[1], 1.1]),
    ]


class CheckMilestoneData:
    @staticmethod
    def checkMilestone(
        data: EMilestone, category: ACategory, milestone, parent: EMilestone = None
    ):
        assert isinstance(data, EMilestone) == True

        assert data.milestone_name == milestone

        idx = category.id if parent == None else parent.id
        assert int(data.id / 10) == idx
