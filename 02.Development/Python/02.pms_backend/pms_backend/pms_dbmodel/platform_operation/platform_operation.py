from pms_dbmodel.common import *
from pms_dbmodel.models.e_platform import EPlatform, EPlatformFamily
from pms_dbmodel.models.a_attribute import ACategory
from pms_dbmodel.operator_operation import logger
from pms_dbmodel.common_operation.common_operation import CommonOperation


class PlatformOperation:
    @classmethod
    def addPlatform(
        cls, id, name, external_name, family: EPlatformFamily, category: ACategory
    ) -> EPlatform:
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

        CommonOperation.setDateAndSave(r)
        return r[0]

    @classmethod
    def getPlatformBasedOnFamily(cls, family) -> list[str]:
        data = EPlatform.objects.filter(platform_family__name=family)

        result = []
        for d in data:
            result.append(d.name)

        return result

    @classmethod
    def getPlatform(cls, name) -> EPlatform:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.getPlatform.__name__,
            "Platform = %s ",
            name,
        )

        return CommonOperation.searchWithName(name, EPlatform)

    @classmethod
    def getPlatforms(cls, family=None) -> list[str]:
        rList = []

        if family == None:
            rList = EPlatform.objects.all()
        else:
            rList = EPlatform.objects.filter(platform_family__name=family)

        result = []
        for r in rList:
            result.append(r.name)

        logInfo(
            logger,
            LOGTIME.END,
            cls.getPlatforms.__name__,
            "Family = %s, Size = %d",
            family,
            len(result),
        )
        return result
