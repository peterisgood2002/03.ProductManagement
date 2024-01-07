from django.test import TestCase
from .services import PlatformService, PlatformParserService
from pathlib import Path
import openpyxl
import logging
from .util import *

logger = logging.getLogger(__name__)


# Create your tests here.
class PlatformParserServiceTest(TestCase):
    def setUp(self) -> None:
        self._getExcel()
        return super().setUp()

    def _getExcel(self):
        path_home = str(Path(__file__).parents[1])
        print("PATH = " + path_home)
        self.fileName = path_home + INPUT_FILE
        self.excel = openpyxl.load_workbook(self.fileName)

    def testParsePlatform(self):
        # PlatformService.parse(self.fileName)
        generation = PlatformParserService.parseGeneration(self.fileName, self.excel)
        assert len(generation) == 4

        family = PlatformParserService.parseFamily(self.fileName, self.excel)
        assert len(family) == 5

        rMap = PlatformParserService.getGenerationMapBasedOnFamily(family)
        assert len(rMap) == 5
        result = PlatformParserService.parsePlatform(self.fileName, self.excel)
        assert len(result) == 4

        dMap = PlatformParserService.getMapAboutPlatformData(result, rMap)

        assert len(dMap) == 2

        gMap = PlatformParserService.getGenerationMapBasedOneID(generation)

        assert len(gMap) == 4
