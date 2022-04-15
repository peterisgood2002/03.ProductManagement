import string
import openpyxl
import re
"""
  Class Items
"""
class Item:
    def __init__(self, fileName, status, capability, id, desc, section):
        self.status = status
        self.capability = capability
        self.id = id
        self.desc = desc
        self.section = section
        self.fileName = fileName
        self.priority = []
        self.type = []
    def __str__(self):
     return self.id

    def addPriority( self, priority):
        self.priority.append(priority)
    def addType( self, t):
        self.type.append(t)
    
"""
  End Class Items
"""
#
def getColumnsBasedOnList( sheet, row, cellValueList: list):
    if( isinstance(cellValueList, list) != True ):
         raise Exception("Note that cellValueList is a list")

    result = cellValueList.copy()

    for col in sheet[row]:
        if col.value:
           index = cellValueList.index(col.value) if col.value in cellValueList else -1
           if index != -1:
                result[index] = col.column_letter
                
    return result

def getColumnsIdxBasedOnList( sheet, row, cellValueList: list):
    if( isinstance(cellValueList, list) != True ):
         raise Exception("Note that cellValueList is a list")

    result = cellValueList.copy()

    for col in sheet[row]:
        if col.value:
           index = cellValueList.index(col.value) if col.value in cellValueList else -1
           if index != -1:
                result[index] = col.col_idx - 1
                
    return result 

def getColumnsBasedOnString( sheet, row, cellValue: str):   
    if( isinstance(cellValue, str) != True ):
        raise Exception("Note that cellValueList is a list")
    for col in sheet[row]:
        if col.value and col.value == cellValue:
            return col.column_letter
def getColumnsIdxBasedOnString( sheet, row, cellValue: str):   
    if( isinstance(cellValue, str) != True ):
        raise Exception("Note that cellValueList is a list")
    for col in sheet[row]:
        if col.value and col.value == cellValue:
            return col.col_idx - 1


"""
 The List of keyColumn should follow the sequence: status, capability, id, desc, section.
 The Priority value depends on the List of productColumn
"""
def getExcelRows( fileName, sheet, dataRow, keyIdx: list, priorityIdx) -> list[Item]:
    print("[getExcelRows][BEGIN]: " + fileName +" ROW = " + str(sheet.max_row))
    if( len(keyIdx) != 5):
        raise Exception("keyColumn should only have 4 elements")
    result = []
    for r in range( dataRow, sheet.max_row):
        id = sheet[r][keyIdx[1]].value
        if id: 
            item = Item(fileName, sheet[r][keyIdx[0]].value, sheet[r][keyIdx[1]].value, sheet[r][keyIdx[2]].value, sheet[r][keyIdx[3]].value, sheet[r][keyIdx[4]].value)
            item.addPriority(sheet[r][priorityIdx[0]].value)
            item.addPriority(sheet[r][priorityIdx[1]].value)
            result.append(item)
    print("[getExcelRows][END]: " + fileName)
    return result
   

