from pms_dbmodel.common import LOGTIME, logInfo, setDateAndSave
from pms_dbmodel.models.e_area import EArea
from pms_dbmodel.operator_operation import logger
from django.db.models.query import QuerySet


class AreaOperation:
    @classmethod
    def getArea(cls, area) -> EArea:
        r = EArea.objects.get_or_create(name=area)
        setDateAndSave(r)

        return r[0]

    @classmethod
    def getIndex(cls, areaId, data: QuerySet):
        result = areaId * 100
        if len(data) != 0:
            result = data[0].id + 1
        return result
