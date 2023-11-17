from pms_dbmodel.models.e_platform import EGeneration
from pms_dbmodel.models.e_platform import EPlatformFamily, EPlatform
from pms_dbmodel.platform import PlatformData
from pms_dbmodel.platform_operation.platform_operation import PlatformOperation


class TestPlatformData:
    # PlatformInformation
    Gen1Id = 1
    Gen1Name = "G1"
    Gen1ExternalName = "Generation 1"
    Gen2Name = "G2"
    categoryId = 1
    category = "TEST"
    family = ["Family1", "Family2"]
    platform = [
        PlatformData([1, Gen1Name, family[0], "Platform1", "P1", category]),
        PlatformData([2, Gen1Name, family[0], "Platform2", "P2", category]),
        PlatformData([3, Gen1Name, family[0], "Platform3", "P3", category]),
        PlatformData([4, Gen1Name, family[1], "Platform4", "P4", category]),
    ]


class CheckPlatformData:
    @staticmethod
    def checkGeneration(gen, id, name):
        assert isinstance(gen, EGeneration)
        assert gen.id == id
        assert gen.name == name

    @staticmethod
    def checkFamily(data: EPlatformFamily, generation, family):
        assert isinstance(data, EPlatformFamily) == True
        assert int(data.id / 10) == data.generation.id
        assert data.name == family
        assert data.generation.name == generation

    @staticmethod
    def checkPlatform(data: EPlatform, ref: PlatformData):
        assert isinstance(data, EPlatform) == True
        assert data.id == ref.getInfo(PlatformData.INFO.ID)
        assert data.name == ref.getInfo(PlatformData.INFO.NAME)
        assert data.external_name == ref.getInfo(PlatformData.INFO.EXTERNAL_NAME)

        assert data.platform_family.name == ref.getInfo(PlatformData.INFO.FAMILY)
        assert data.category.category_name == ref.getInfo(PlatformData.INFO.CATEGORY)

    @staticmethod
    def checkPlatforms(count, family):
        rList = PlatformOperation.getPlatformBasedOnFamily(TestPlatformData.family[0])

        assert len(rList) == 3
