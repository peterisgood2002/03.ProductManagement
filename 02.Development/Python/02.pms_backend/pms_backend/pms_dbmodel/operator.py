from enum import Enum
from pms_dbmodel.operator_operation import logger
from pms_dbmodel.common import LOGTIME, logInfo


class OperatorRequirement:
    class INFO(Enum):
        VERSION = 0
        ChapterId = 1
        Chapter = 2
        SectionId = 3
        Section = 4
        TAG = 5
        TITLE = 6
        NAME = 7
        DESC = 8

    def __init__(self, requirement):
        self._requirement = requirement

    def getInfo(self, info: INFO):
        return self._requirement[info.value]


class OperatorOperationFacade:
    @classmethod
    def addOperatorRequirements(
        cls, operator, version, requirements: list[OperatorRequirement]
    ):
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addOperatorRequirements.__name__,
            "Operator = %s, Version = %s, Size = ",
            operator,
            version,
            len(requirements),
        )

        #
