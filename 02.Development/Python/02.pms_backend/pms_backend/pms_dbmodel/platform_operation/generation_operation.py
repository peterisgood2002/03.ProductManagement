from pms_dbmodel.common import *
from pms_dbmodel.models.e_platform import EGeneration
from pms_dbmodel.platform_operation import logger
from pms_dbmodel.common_operation.common_operation import CommonOperation


class GenerationOperation:
    @classmethod
    def addGerneration(cls, id, name, externalName=None) -> tuple[EGeneration, bool]:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addGerneration.__name__,
            "Id = %s, Name = %s ExternalName = %s",
            id,
            name,
            externalName,
        )

        result = EGeneration.objects.get_or_create(id=id)

        result[0].name = name

        if externalName != None:
            result[0].external_name = externalName
        CommonOperation.setDateAndSave(result)

        return result

    @classmethod
    def getGeneration(cls, name) -> EGeneration:
        logInfo(logger, LOGTIME.BEGIN, cls.getGeneration.__name__, "Name = %s", name)

        return CommonOperation.searchWithName(name, EGeneration)
