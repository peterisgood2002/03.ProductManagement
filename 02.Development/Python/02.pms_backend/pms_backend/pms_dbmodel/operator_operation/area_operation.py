from pms_dbmodel.common import LOGTIME, logInfo, setDateAndSave
from pms_dbmodel.models.e_operator import EArea
from pms_dbmodel.operator_operation import logger


class AreaOperation:
    @classmethod
    def getArea(cls, area) -> EArea:
        r = EArea.objects.get_or_create(name=area)
        setDateAndSave(r)

        return r[0]
