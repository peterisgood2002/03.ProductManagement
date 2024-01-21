from pms_dbmodel.common import *
from pms_dbmodel.models.a_attribute import ACategory
from pms_dbmodel.common_operation import logger
from .common_operation import CommonOperation
from enum import Enum


class Category(Enum):
    Platform = 1
    Customer = 2
    Product = 3
    Milestone = 4


class CategoryOperation:
    @classmethod
    def addCategory(cls, id, category) -> ACategory:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addCategory.__name__,
            "ID = %d, Category = %s",
            id,
            category,
        )

        r = ACategory.objects.get_or_create(id=id)

        r[0].category_name = category

        CommonOperation.setDateAndSave(r)

        return r[0]

    @classmethod
    def addCategoryWithParent(cls, category, parent: ACategory) -> ACategory:
        data = ACategory.objects.filter(
            parent=parent,
        ).order_by("-id")

        result = None

        for d in data:
            if d.category_name == category:
                result = d

        if result == None:
            index = CommonOperation.getIntegerIndex(parent.id * 10, data)
            r = ACategory.objects.get_or_create(id=index)
            r[0].category_name = category
            r[0].parent = parent
            CommonOperation.setDateAndSave(r)

            result = r[0]

        return result

    @classmethod
    def getCategoryMap(cls) -> dict[str, ACategory]:
        data = ACategory.objects.all()

        return CategoryOperation._getMap(data)

    @staticmethod
    def _getMap(data):
        result = {}

        for d in data:
            result[d.category_name] = d

        return result

    @classmethod
    def getCategoryMapBasedOn(cls, category) -> dict[str, ACategory]:
        data = ACategory.objects.filter(parent=category)

        return CategoryOperation._getMap(data)
