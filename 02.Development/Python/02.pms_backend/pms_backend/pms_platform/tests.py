from django.test import TestCase
from .services import PlatformService
from pathlib import Path
import openpyxl
import logging
from .util import *

logger = logging.getLogger(__name__)


# Create your tests here.
class PlatformServiceTest(TestCase):
    def setUp(self) -> None:
        self._getExcel()
        return super().setUp()

    def _getExcel(self):
        path_home = str(Path(__file__).parents[1])
        print("PATH = " + path_home)
        self.fileName = path_home + INPUT_FILE
        self.excel = openpyxl.load_workbook(self.fileName)

    def testParseGeneration(self):
        # PlatformService.parse(self.fileName)
        generation = PlatformService.parseGeneration(self.fileName, self.excel)
        assert len(generation) == 4

        family = PlatformService.parseFamily(self.fileName, self.excel)
        assert len(family) == 5

        rMap = PlatformService.getGenerationMapBasedOnFamily(family)
        assert len(rMap) == 5
        result = PlatformService.parsePlatform(self.fileName, self.excel)
        assert len(result) == 4

        dMap = PlatformService.getMapAboutPlatformData(result, rMap)

        assert len(dMap) == 2

        PlatformService.addPlatforms(generation, dMap, self._test)

        gMap = PlatformService.getGenerationMapBasedOneID(generation)

        PlatformService.updateFamilyExternal(family, self._testFamilyExternal)

        assert len(gMap) == 4

    def _test(self, id, gName, external, data: list):
        logger.info(
            "[_test] id = %s, name = %s, external = %s, data = %d",
            id,
            gName,
            external,
            len(data),
        )

    def _testFamilyExternal(self, name, external):
        logger.info(
            "[_testFamilyExternal]  name = %s, external = %s",
            name,
            external,
        )
