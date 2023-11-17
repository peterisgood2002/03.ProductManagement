from pms_dbmodel.common import LOGTIME, logInfo, setDateAndSave
from pms_dbmodel.models.e_platform import EGeneration
from pms_dbmodel.platform_operation import logger
from pms_dbmodel.common import LOGTIME, logInfo, setDateAndSave


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

        if result[1] == True:
            result[0].name = name
            result[0].external_name = externalName
        setDateAndSave(result)

        return result

    @classmethod
    def getGeneration(cls, name) -> EGeneration:
        logInfo(logger, LOGTIME.BEGIN, cls.getGeneration.__name__, "Name = %s", name)

        gList = EGeneration.objects.filter(name=name)
        if len(gList) == 0:
            return None

        return gList[0]
