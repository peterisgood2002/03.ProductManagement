# Create your models here.

from pms_dbmodel.models.e_area import EArea
from pms_dbmodel.models.e_operator import EOperator
from pms_dbmodel.operator_operation import logger
from .area_operation import AreaOperation

from pms_dbmodel.common import *
from pms_dbmodel.common_operation.common_operation import CommonOperation


class OperatorOperation:
    @classmethod
    def addOperator(cls, area, operator) -> EOperator:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addOperator.__name__,
            "AREA = %s, Operator = %s",
            area,
            operator,
        )

        a: EArea = AreaOperation.getArea(area)

        if a == None:
            raise Exception("We do not have this area:" + area)
        operators = EOperator.objects.filter(area=a).order_by("-id")

        result = None

        for o in operators:
            if o.name == operator:
                result = o

        if result == None:
            index = CommonOperation.getIndex(a.id * 100, operators)

            r = EOperator.objects.get_or_create(id=index, name=operator, area=a)
            CommonOperation.setDateAndSave(r)
            result = r[0]

        logInfo(
            logger,
            LOGTIME.END,
            cls.addOperator.__name__,
            "[END] Result = %d",
            result.id,
        )

        return result

    @classmethod
    def getOperator(cls, operator) -> EOperator:
        logInfo(
            logger, LOGTIME.BEGIN, cls.getOperator.__name__, "Operator = %s", operator
        )
        return CommonOperation.searchWithName(operator, EOperator)
