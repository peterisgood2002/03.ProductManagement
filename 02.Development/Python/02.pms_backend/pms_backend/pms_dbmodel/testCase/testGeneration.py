from .base_test import PMSDbTest
from pms_dbmodel.models.e_platform import EGeneration
from pms_dbmodel.platform_operation.generation_operation import GenerationOperation
from pms_dbmodel.testplatformdata import TestPlatformData, CheckPlatformData


class GenerationOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(EGeneration)

    def testAddGerneration(self):
        r = GenerationOperation.addGerneration(
            TestPlatformData.Gen1Id,
            TestPlatformData.Gen1Name,
            TestPlatformData.Gen1ExternalName,
        )
        CheckPlatformData.checkGeneration(
            r[0], TestPlatformData.Gen1Id, TestPlatformData.Gen1Name
        )
        gen = GenerationOperation.getGeneration(TestPlatformData.Gen1Name)
        CheckPlatformData.checkGeneration(
            gen, TestPlatformData.Gen1Id, TestPlatformData.Gen1Name
        )

        gen = GenerationOperation.getGeneration(TestPlatformData.Gen2Name)
        assert gen == None
