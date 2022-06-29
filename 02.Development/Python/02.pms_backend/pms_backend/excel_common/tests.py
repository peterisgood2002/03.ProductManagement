import os
from django.test import TestCase
import unittest
from pathlib import Path
import openpyxl

from excel_common.excel_operation import ExcelParser
from excel_common.excel_operation import KEYINFO
# Create your tests here.

class ExcelParserTest(TestCase):
    
    def test(self):
        print('TEST')
            
    def setUp(self) -> None:
        self._getParser()
        self._getExcel()
        return super().setUp()   
    
    def _getParser(self):
        self.keyMap = {
            KEYINFO.Id: "Global ID", 
            KEYINFO.Description:  "Description", 
            KEYINFO.Status: "Status", 
            KEYINFO.ChapterId:"Heading", 
            KEYINFO.Chapter: "Name", 
            KEYINFO.SectionId: "Heading", 
            KEYINFO.Section: "Name",
            KEYINFO.DocLocation:"TRD",
            KEYINFO.Priority: "Priority",
            KEYINFO.Note:"OEM Compliance"
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
        
        self.assertIsNotNone( t.keyMap )
        self.assertIsNotNone( t.typeMap )
        self.assertEqual(0, len(t.keyMap) )
        self.assertEqual(0, len(t.typeMap) )
        self.assertEqual(0, t.keyRow )
        self.assertEqual(0, t.typeRow)
        
    def testConstructor(self):
        self.assertCountEqual(self.productType, self.t._originalProductTypeList)
        self.assertCountEqual(self.keyMap, self.t._originalKeyMap )
        
        # Copy
        self.productType.clear()
        self.keyMap.clear()
        self.assertNotEqual(self.productType, self.t._originalProductTypeList)
        self.assertNotEqual(self.keyMap, self.t._originalKeyMap)
        
        # Int
        self.assertEqual(2, self.t.keyRow)
        self.assertEqual(3, self.t.typeRow)
    
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
            KEYINFO.Note: 17
        }
        typeResult = {"TEST": 6}
        self.assertEqual( keyResult, self.t.keyMap)
        self.assertEqual( typeResult, self.t.typeMap)
        
    
    def testGetItem(self):
        self.t.createMap(self.sheet)
        items = self.t.parse( self.fileName, "TEST", 4)
        self.assertEqual("TEST_ID",items[0].getId() )
        self.assertEqual("TEST_DESC", items[0].getKey( KEYINFO.Description) )
        self.assertEqual(3.1, items[0].getChapterId() )
        self.assertEqual("TEST_Name", items[0].getChapter() )
        self.assertEqual("TEST_TRD", items[0].getKey(KEYINFO.DocLocation) )
        self.assertEqual("Mandatory", items[0].getPriority() )
        self.assertEqual("Yes", items[0].getKey(KEYINFO.Note) )
        i = 0    
    
    def tearDown(self) -> None:
        self.excel.close()
        return super().tearDown()