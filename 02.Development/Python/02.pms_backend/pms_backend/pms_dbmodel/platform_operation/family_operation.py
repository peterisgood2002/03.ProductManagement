from pms_dbmodel.models.e_platform import EPlatformFamily, EGeneration
from pms_dbmodel.common import *
from pms_dbmodel.platform_operation import logger
from pms_dbmodel.platform_operation.generation_operation import GenerationOperation
from pms_dbmodel.common_operation.common_operation import CommonOperation


class PlatformFamilyOperation:
    @classmethod
    def addPlatformFamily(cls, genName, familyName) -> EPlatformFamily:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addPlatformFamily.__name__,
            "Generation = %s, Family = %s",
            genName,
            familyName,
        )
        gen: EGeneration = GenerationOperation.getGeneration(genName)

        if gen == None:
            raise Exception("We do not get Generation:" + genName)

        families = EPlatformFamily.objects.filter(generation=gen).order_by("-id")
        result = None

        for f in families:
            if f.name == familyName:
                result = f

        if result == None:
            index = CommonOperation.getIndex(gen.id * 10, families)

            r = EPlatformFamily.objects.get_or_create(
                id=index, name=familyName, generation=gen
            )
            CommonOperation.setDateAndSave(r)
            result = r[0]

        logInfo(
            logger,
            LOGTIME.END,
            cls.addPlatformFamily.__name__,
            "[END] Result = %d",
            result.id,
        )

        return result

    @classmethod
    def updatePlatformFamilyExternalName(cls, family, name) -> EPlatformFamily:
        logInfo(
            logger,
            LOGTIME.BEGIN,
            cls.addPlatformFamily.__name__,
            "Family = %s, External = %s",
            family,
            name,
        )

        result = EPlatformFamily.objects.get(name=family)

        result.external_name = name

        CommonOperation.setDateAndSave(result)
        return result

    @classmethod
    def getFamiliesBasedOnGen(cls, genName) -> list[str]:
        families = cls.getFamilies(genName)

        result = []
        for f in families:
            result.append(f.name)

        logInfo(
            logger,
            LOGTIME.END,
            cls.getFamiliesBasedOnGen.__name__,
            "[END] Generation = %s, Result = %d",
            genName,
            len(result),
        )
        return result

    @classmethod
    def getFamilies(cls, genName):
        gen = GenerationOperation.getGeneration(genName)

        families = EPlatformFamily.objects.filter(generation=gen)
        return families

    @classmethod
    def getFamilyMapBasedOnGen(cls, genName) -> dict[str, EPlatformFamily]:
        families = cls.getFamilies(genName)
        result = {}

        for f in families:
            result[f.name] = f

        return result
