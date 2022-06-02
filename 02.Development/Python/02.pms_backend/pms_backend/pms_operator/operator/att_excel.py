from email import utils
import logging
import os
import shutil
import string

import openpyxl
from excel_common.excel_operation import ExcelParser, KEYINFO
from excel_common.excel_operation import Item
from .utils import INPUT_FOLDER

logger = logging.getLogger("ExcelParser")

def _getATTCompliance( fileName, sheetName, excel ) -> list[Item]:
    logging.info("[_getATTCompliance][Begin]")
    keyMap = {
        KEYINFO.Id: "Requirement TAG", 
        KEYINFO.Description:  "Description", 
        KEYINFO.Status: "Status", 
        KEYINFO.ChapterId:"Chapter No.", 
        KEYINFO.Chapter: "Chapter Name", 
        KEYINFO.SectionId: "Section No.", 
        KEYINFO.Section: "Section Name",
        KEYINFO.Priority: "Priority",
    }
        
    sheet = excel[sheetName]
    
    parser = ExcelParser(keyRow=13, originalKeyMap = keyMap)
    parser.createMap(sheet)
    
    result = parser.parseExcel( fileName, 14, sheet)
    logging.info("[_getATTCompliance][End] result = {0}", len(result))
    return result 

def _getATTItems( fileName):
    
    excel = openpyxl.load_workbook( fileName )
    items = _getATTCompliance(fileName, "COMPLIANCE MATRIX", excel)


#
def att_excel_parser(srcName: string, version):
    if os.path.isdir( INPUT_FOLDER) == False:
        os.makedirs(INPUT_FOLDER)
        
    #1. Move file to folder
    desName = INPUT_FOLDER + os.path.basename(srcName)
    #shutil.move(srcName, desName)
    #2. Parse file and Get Item
    _getATTItems(desName)