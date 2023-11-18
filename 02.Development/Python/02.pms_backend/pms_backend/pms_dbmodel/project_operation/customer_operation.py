from pms_dbmodel.models.e_area import EArea
from pms_dbmodel.project_operation import logger
from pms_dbmodel.common import LOGTIME, logInfo, setDateAndSave

from pms_dbmodel.operator_operation.area_operation import AreaOperation
from pms_dbmodel.models.e_customers import ECustomer


class CustomerOperation:
    @classmethod
    def addCustomer(cls, area, customer, alpha=False):
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addCustomer.__name__,
            "AREA = %s, Customer = %s",
            area,
            customer,
        )

        a: EArea = AreaOperation.getArea(area)

        if a == None:
            raise Exception("We do not have this area:" + area)

        customers = ECustomer.objects.filter(area=a).order_by("-id")

        result = None

        for c in customers:
            if c.name == customer:
                result = customer

        if result == None:
            index = AreaOperation.getIndex(a.id, customers)

            r = ECustomer.objects.get_or_create(
                id=index, name=customer, area=a, is_alpha=alpha
            )
            setDateAndSave(r)
            result = r[0]

        logInfo(
            logger,
            LOGTIME.END,
            cls.addCustomer.__name__,
            "[END] Result = %d",
            result.id,
        )

        return result

    @classmethod
    def getCustomers(cls, area=None) -> list[str]:
        rList = []
        if area == None:
            rList = ECustomer.objects.all()

        else:
            rList = ECustomer.objects.filter(area=area)

        result = []
        for r in rList:
            result.append(r.name)

        logInfo(
            logger,
            LOGTIME.END,
            cls.getCustomers.__name__,
            "AREA = %s, Size = %d",
            area,
            len(result),
        )
        return result

    @classmethod
    def getCustomer(cls, customer) -> ECustomer:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.getCustomer.__name__,
            "Customer = %s",
            customer,
        )

        rList = ECustomer.objects.filter(name=customer)
        if len(rList) == 0:
            return None
        return rList[0]
