from pms_dbmodel.common_operation.category_operation import (
    CategoryOperation,
)
from .base_test import PMSDbTest
from pms_dbmodel.models.e_platform import EPlatform
from pms_dbmodel.models.a_attribute import ACategory
from pms_dbmodel.platform_operation.platform_operation import (
    PlatformOperation,
)
from pms_dbmodel.platform_operation.generation_operation import GenerationOperation
from pms_dbmodel.platform_operation.family_operation import PlatformFamilyOperation
from pms_dbmodel.testplatformdata import TestPlatformData, CheckPlatformData
from pms_dbmodel.platform import PlatformData


class PlatformOperationTest(PMSDbTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            ACategory,
            EPlatform,
        )

    def testPlatform(self):
        r = GenerationOperation.addGerneration(
            TestPlatformData.Gen1Id,
            TestPlatformData.Gen1Name,
            TestPlatformData.Gen1ExternalName,
        )

        for data in TestPlatformData.platform:
            generation = data.getInfo(PlatformData.INFO.GENERATION)
            family = data.getInfo(PlatformData.INFO.FAMILY)
            f = PlatformFamilyOperation.addPlatformFamily(generation, family)

            id = data.getInfo(PlatformData.INFO.ID)
            platform = data.getInfo(PlatformData.INFO.NAME)
            external = data.getInfo(PlatformData.INFO.EXTERNAL_NAME)
            category = data.getInfo(PlatformData.INFO.CATEGORY)

            c = CategoryOperation.addCategory(TestPlatformData.categoryId, category)
            r = PlatformOperation.addPlatform(id, platform, external, f, c)

            CheckPlatformData.checkPlatform(r, data)

        CheckPlatformData.checkPlatforms(3, TestPlatformData.family[0])
