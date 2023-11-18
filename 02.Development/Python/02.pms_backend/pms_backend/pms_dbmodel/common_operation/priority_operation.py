from pms_dbmodel.common import *
from pms_dbmodel.models.a_attribute import APriority
from pms_dbmodel.common_operation import logger
from enum import Enum
from pms_dbmodel.common_operation.common_operation import CommonOperation


class PriorityCategory(Enum):
    Mandatory = 0
    Optional = 1


class PriorityOperation:
    @classmethod
    def addPriority(cls, priority) -> tuple[APriority, bool]:
        logInfo(
            logger, LOGTIME.BEGIN, cls.addPriority.__name__, "Priority = %s", priority
        )

        r = APriority.objects.get_or_create(name=priority)

        CommonOperation.setDateAndSave(r)

        return r

    @classmethod
    def getPriorityMap(cls) -> dict[str, APriority]:
        result = {}

        data = APriority.objects.all()

        for d in data:
            result[d.name] = d

        logInfo(
            logger, LOGTIME.END, cls.getPriorityMap.__name__, "Size = %s", len(result)
        )
        return result
