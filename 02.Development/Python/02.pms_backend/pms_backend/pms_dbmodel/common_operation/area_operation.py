from pms_dbmodel.common import *
from pms_dbmodel.models.e_area import EArea
from pms_dbmodel.operator_operation import logger
from pms_dbmodel.common_operation.common_operation import CommonOperation


class AreaOperation:
    @classmethod
    def getArea(cls, area) -> EArea:
        r = EArea.objects.get_or_create(name=area)
        CommonOperation.setDateAndSave(r)

        return r[0]
