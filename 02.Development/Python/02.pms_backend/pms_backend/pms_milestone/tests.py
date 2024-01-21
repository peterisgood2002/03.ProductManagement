from django.test import TestCase
import logging
from .util import *
from pathlib import Path
import openpyxl

from .services import MilestoneParserService

logger = logging.getLogger(__name__)


# Create your tests here.
class MilestoneServiceTest(TestCase):
    def setUp(self) -> None:
        self._getExcel()
        return super().setUp()

    def _getExcel(self):
        path_home = str(Path(__file__).parents[1])
        print("PATH = " + path_home)
        self.fileName = path_home + HOME_INPUT_FILE
        self.excel = openpyxl.load_workbook(self.fileName)
        i = 0

    def testParseMilestone(self):
        data = MilestoneParserService.parseMilestone(self.fileName, self.excel)

        assert 9 == len(data)

        result = MilestoneParserService.createMilestoneData(data)
        assert 9 == len(result)
