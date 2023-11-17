from .base_test import PMSDbTest

from pms_dbmodel.models.e_platform import EPlatformFamily, EGeneration
from pms_dbmodel.platform_operation.family_operation import PlatformFamilyOperation
from pms_dbmodel.platform_operation.generation_operation import GenerationOperation
from pms_dbmodel.testplatformdata import TestPlatformData, CheckPlatformData
from pms_dbmodel.platform import PlatformData


class PlatformFamilyOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(EGeneration, EPlatformFamily)

    def testAddFamily(self):
        GenerationOperation.addGerneration(
            TestPlatformData.Gen1Id,
            TestPlatformData.Gen1Name,
            TestPlatformData.Gen1ExternalName,
        )

        for f in TestPlatformData.platform:
            generation = f.getInfo(PlatformData.INFO.GENERATION)
            family = f.getInfo(PlatformData.INFO.FAMILY)
            r = PlatformFamilyOperation.addPlatformFamily(generation, family)
            CheckPlatformData.checkFamily(r, generation, family)
        result = PlatformFamilyOperation.getFamiliesBasedOnGen(
            TestPlatformData.Gen1Name
        )

        assert len(result) == 2

        family = TestPlatformData.platform[0].getInfo(PlatformData.INFO.FAMILY)
        external = "Test"
        f = PlatformFamilyOperation.updatePlatformExternalName(family, external)
        result = EPlatformFamily.objects.get(name=family)
        assert external == result.external_name
