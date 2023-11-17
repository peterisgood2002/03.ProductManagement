from pms_dbmodel.common import LOGTIME, logInfo, setDateAndSave
from pms_dbmodel.models.e_platform import EPlatform, EPlatformFamily
from pms_dbmodel.models.a_attribute import ACategory
from pms_dbmodel.operator_operation import logger


class CategoryOperation:
    @classmethod
    def addCategory(cls, id, category) -> tuple[ACategory, bool]:
        logInfo(
            logger, LOGTIME.BEGIN, cls.addCategory.__name__, "Category = %s", category
        )

        r = ACategory.objects.get_or_create(id=id)

        r[0].category_name = category

        setDateAndSave(r)

        return r

    @classmethod
    def getCategoryMap(cls) -> dict[str, ACategory]:
        data = ACategory.objects.all()

        result = {}

        for d in data:
            result[d.category_name] = d

        return result


class PlatformOperation:
    @classmethod
    def addPlatform(
        cls, id, name, external_name, family: EPlatformFamily, category: ACategory
    ):
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addPlatform.__name__,
            "Id = %d, Family = %s, name = %s, external_name = %s",
            id,
            family.name,
            name,
            external_name,
        )

        r = EPlatform.objects.get_or_create(
            id=id, platform_family=family, category=category
        )

        r[0].name = name
        r[0].external_name = external_name

        setDateAndSave(r)
        return r

    @classmethod
    def getPlatformBasedOnFamily(cls, family) -> list[str]:
        data = EPlatform.objects.filter(platform_family__name=family)

        result = []
        for d in data:
            result.append(d.name)

        return result
