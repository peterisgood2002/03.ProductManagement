# Create your models here.

from pms_dbmodel.models.e_operator import EArea, EOperator
from pms_dbmodel.operator_operation import logger
from .area_operation import AreaOperation

from pms_dbmodel.common import LOGTIME, logInfo, setDateAndSave


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
        operators = EOperator.objects.filter(area=a).order_by("-id")

        result = None

        for o in operators:
            if o.name == operator:
                result = o

        if result == None:
            index = a.id * 100
            if len(operators) != 0:
                index = operators[0].id + 1
            r = EOperator.objects.get_or_create(id=index, name=operator, area=a)
            setDateAndSave(r)
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
        operator = EOperator.objects.filter(name=operator)

        if len(operator) == 0:
            return None
        return operator[0]