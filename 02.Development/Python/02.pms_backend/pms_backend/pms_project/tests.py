from django.test import TestCase
from .services import ProjectParserService
import logging
from .util import *
from pathlib import Path
import openpyxl

logger = logging.getLogger(__name__)


# Create your tests here.
class ProjectServiceTest(TestCase):
    def setUp(self) -> None:
        self._getExcel()
        return super().setUp()

    def _getExcel(self):
        path_home = str(Path(__file__).parents[1])
        print("PATH = " + path_home)
        self.fileName = path_home + HOME_INPUT_FILE
        self.excel = openpyxl.load_workbook(self.fileName)
        i = 0

    def testCollectIntoOneExcel(self):
        path_home = str(Path(__file__).parents[1])
        print("PATH = " + path_home)
        pass
        """
        ProjectParserService.collectIntoOneExcel(
            path_home + HOME_INPUT_FILE,
            path_home + L1_INPUT_FILE,
            path_home + L2_INPUT_FILE,
            path_home + L3_INPUT_FILE,
        )
        """

    def testParseProject(self):
        home = ProjectParserService.parseHomeProject(self.fileName, self.excel)
        assert len(home) == 3
        L1 = ProjectParserService.parseL1Project(self.fileName, self.excel)
        assert len(L1) == 1

        L2 = ProjectParserService.parseL2Project(self.fileName, self.excel)
        assert len(L2) == 2
        L3 = ProjectParserService.parseL3Project(self.fileName, self.excel)
        assert len(L3) == 2

        result = ProjectParserService.getAllItem(self.fileName)
        assert len(result) == 8

        platform = ProjectParserService.getAllPlatforms(result)

        assert len(platform) == 3

        customers = ProjectParserService.getAllCustomers(result)

        assert len(customers) == 4
        customerAreaMap = {
            "Home": ["TW"],
            "Customer1": ["TW"],
            "Customer3": ["EU"],
            "Customer2": ["CN"],
        }
        project = ProjectParserService.createProjectData(result, customerAreaMap)
        assert len(project) == 4
