from email import utils
import logging
import os
import shutil
import string

import openpyxl
from excel_common.excel_operation import ExcelParser, KEYINFO
from excel_common.excel_operation import Item
from excel_common.util import ItemType
from .utils import INPUT_FOLDER

logger = logging.getLogger("ExcelParser")

def _getATTCompliance( fileName, sheetName, excel ) -> list[Item]:
    logging.info("[_getATTCompliance][Begin]")
    keyMap = {
        KEYINFO.Id: "Requirement TAG", 
        KEYINFO.Title:  "Description", 
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
    logging.info("[_getATTCompliance][End] result = %d", len(result))
    return result 

def _getATTChange( fileName, sheetName, type: ItemType, excel) -> dict:
    logging.info("[_getATTChange][Begin] SheetName = " + sheetName + " Type = " + type.name)
    keyMap = {
        KEYINFO.Id: "Device Feature Number", 
        KEYINFO.Title: "Title",
        KEYINFO.Description: "Description",
        KEYINFO.Note:"Change Description"
    }
    
    sheet = excel[sheetName]
    parser = ExcelParser(keyRow=1, originalKeyMap = keyMap)
    parser.createMap(sheet)
    
    items = parser.parseExcel( fileName, 2, sheet)
    logging.info("[_getATTChange][End] result = %d", len(items))
    
    result = {}
    
    for i in items:
        id = i.getId()
        result[id] = i
    return result
 
def _addToMap( result: dict, type:ItemType, item:Item):
    items:list = result.get(type)
    if items == None:
        items = []
        result[type] = items
    
    items.append(item)
       
def _group( fileName, version, excel, items: list[Item], ):
    #1. getChange Items
    text = "13340 {:.1f} Added"
    addedItems = _getATTChange( fileName, text.format(version), ItemType.NEW, excel)
    text = "13340 {:.1f} Modified"
    updateItems = _getATTChange( fileName, text.format(version), ItemType.UPDATE, excel)
    text = "13340 {:.1f} Deleted"
    deletedItems = _getATTChange( fileName, text.format(version), ItemType.DELETE, excel)
    #2. Group
    result = {}
    
    for item in items:
        id = item.getId()
        #1. Find Status
        status = ItemType.NOCHANGE
        change = None
        if addedItems.get(id) != None:
            change = addedItems.get(id)
            status = ItemType.NEW
        elif updateItems.get(id) != None:
            change = updateItems.get(id)
            status = ItemType.UPDATE
        elif deletedItems.get(id) != None:
            change = deletedItems.get(id)
            status = ItemType.DELETE
        
        #2. Change Item
        desc = ""
        if change != None:
           desc = change.getKey(KEYINFO.Description)
        
        item.setKey(KEYINFO.Description, desc)
        item.setKey(KEYINFO.Status, status)
        #3. add into result
        _addToMap(result, status, item)    
   
    return result
    
def _getATTItems( fileName, version, isFirstTime = False) -> dict:
    
    excel = openpyxl.load_workbook( fileName )
    items = _getATTCompliance(fileName, "COMPLIANCE MATRIX", excel)
    
    #TODO Group items into 4 group: New, Update, Delete, and No-Change items
    result = {}
    
    if isFirstTime == True:
        result[ItemType.NEW] = items
    else: result = _group(fileName, version, excel, items)
    return result

#
def att_excel_parser(srcName: string, version, isFirstTime = False) -> dict:
    if os.path.isdir( INPUT_FOLDER) == False:
        os.makedirs(INPUT_FOLDER)
        
    #1. Move file to folder
    desName = INPUT_FOLDER + os.path.basename(srcName)
    #shutil.move(srcName, desName)
    #2. Parse file and Get Item
    return _getATTItems(desName, version, isFirstTime)