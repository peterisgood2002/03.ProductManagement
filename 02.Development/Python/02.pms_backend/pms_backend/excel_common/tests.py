import os
from django.test import TestCase
import unittest
from pathlib import Path
import openpyxl

from excel_common.excel_operation import ExcelParser
from excel_common.excel_operation import KEYINFO
from excel_common.excel_operation import NOCOLUMNINX

# Create your tests here.


class ExcelParserTest(TestCase):
    def test(self):
        print("TEST")

    def setUp(self) -> None:
        self._getParser()
        self._getExcel()
        return super().setUp()

    def _getParser(self):
        self.keyMap = {
            KEYINFO.Id: "Global ID",
            KEYINFO.Description: "Description",
            KEYINFO.Status: "Status",
            KEYINFO.ChapterId: "Heading",
            KEYINFO.Chapter: "Name",
            KEYINFO.SectionId: "Heading",
            KEYINFO.Section: "Name",
            KEYINFO.DocLocation: "TRD",
            KEYINFO.Priority: "Priority",
            KEYINFO.Note: "OEM Compliance",
        }

        self.productType = ["TEST"]

        self.t = ExcelParser(2, self.keyMap, 3, self.productType)

    def _getExcel(self):
        path_home = str(Path(__file__).parents[1])
        print("PATH = " + path_home)
        self.fileName = path_home + "./excel_common/input_test/test.xlsx"
        self.excel = openpyxl.load_workbook(self.fileName)
        self.sheet = self.excel["TEST"]

    def testDefaultConstructor(self):
        t = ExcelParser()

        assert t.keyMap != None
        assert t.typeMap != None
        assert 0 == len(t.keyMap)
        assert 0 == len(t.typeMap)
        assert 0 == t.keyRow
        assert 0 == t.typeRow

    def testConstructor(self):
        self.assertCountEqual(self.productType, self.t._originalProductTypeList)
        self.assertCountEqual(self.keyMap, self.t._originalKeyMap)

        # Copy
        self.productType.clear()
        self.keyMap.clear()
        assert self.productType != self.t._originalProductTypeList
        assert self.keyMap != self.t._originalKeyMap

        # Int
        assert 2 == self.t.keyRow
        assert 3 == self.t.typeRow

    def testCreateMap(self):
        self.t.createMap(self.sheet)

        keyResult = {
            KEYINFO.Id: 3,
            KEYINFO.Description: 5,
            KEYINFO.Status: -1,
            KEYINFO.ChapterId: 1,
            KEYINFO.Chapter: 2,
            KEYINFO.SectionId: 1,
            KEYINFO.Section: 2,
            KEYINFO.DocLocation: 0,
            KEYINFO.Priority: 4,
            KEYINFO.Note: 17,
        }
        typeResult = {"TEST": 6}

        for k in self.t.keyMap.keys():
            if keyResult.get(k) != None:
                assert keyResult[k] == self.t.keyMap[k]
            else:
                assert NOCOLUMNINX == self.t.keyMap[k]

        assert typeResult == self.t.typeMap

    def testGetItem(self):
        self.t.createMap(self.sheet)
        items = self.t.parse(self.fileName, "TEST", 4)
        #        assert "TEST_ID" == items[0].getId()
        assert "TEST_DESC" == items[0].getKey(KEYINFO.Description)
        assert 3.1 == items[0].getChapterId()
        assert "TEST_Name" == items[0].getChapter()
        assert "TEST_TRD" == items[0].getKey(KEYINFO.DocLocation)
        assert "Mandatory" == items[0].getPriority()
        assert "Yes" == items[0].getKey(KEYINFO.Note)

    def tearDown(self) -> None:
        self.excel.close()
        return super().tearDown()
