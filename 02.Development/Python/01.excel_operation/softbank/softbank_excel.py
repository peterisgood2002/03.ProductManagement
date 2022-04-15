
from typing import Dict
from common import excel_operation
from common import file_operation
import openpyxl
import time
import datetime


"""
getItemsFromExcel
"""
#addToMap Function
def addToMap( items: list[ excel_operation.Item ], itemMap: dict ):
    for item in items:
        if item.status != "Delete":
           itemMap[item.id] = item
#End addToMap Function
def getItemsFromExcel( fileName: list, sheetName, keyColumnName: list, productType: list ):
    #2.1 Get Critical Column
    #capability, id, desc, section, priority  
    excel = openpyxl.load_workbook(fileName[0])
    sheet = excel[sheetName]
    keyIdx = excel_operation.getColumnsIdxBasedOnList(sheet, 4, keyColumnName)
    
    productIdx=  excel_operation.getColumnsIdxBasedOnList(sheet,3, productType)

    result = {}
  
    beginT = str(datetime.datetime.now())
#fileName = ["D:\\02.Operator\\02.Softbank\\02.Operator Terminal Requirements\\OTR-2022.Q2.Q3\\OTR-20210730_FullPackage\\02_Conformance_sheet\\OTR-MTC-MTC_THP-CONF-RevD01-20210226_E.xlsx"]
    for f in fileName:
        print("open: " + f)
        excel = openpyxl.load_workbook(f)
        sheet = excel[sheetName]
        items = excel_operation.getExcelRows(f, sheet, 5, keyIdx, productIdx)
        print("addToMap: " + f)
        addToMap(items, result)

        excel.close()
        print("finish: " + f)
    #items.append( getItems(sheet, keyColumn, productColumn) )
    endT = str(datetime.datetime.now())
    print(beginT)
    print(endT)

    return result
"""
End getItemsFromExcel
"""

"""   
outputExcel
"""
def outputExcel( outputFileName, productType: list, itemMap: dict  ):
    wb  = openpyxl.Workbook()
    sheet = wb.active
    sheet.cell(row=1, column=1).value = "Id"
    sheet.cell(row=1, column=2).value = "Description"
    sheet.cell(row=1, column=3).value = "Section"
    sheet.cell(row=1, column=4).value = "FileName"
    c = 5
    for p in productType:
        sheet.cell(row=1, column=c).value = p
        c += 1

    r = 2
    for item in itemMap.values():
    
        sheet.cell(row=r, column=1).value = item.id
        sheet.cell(row=r, column=2).value = item.desc
        sheet.cell(row=r, column=3).value = item.section
        c = 4
        for p in item.priority:
            sheet.cell(row=r, column=c).value = p
            c += 1
        sheet.cell(row=r, column=c).value = item.fileName
        r += 1
   
    wb.save(outputFileName)
"""   
End outputExcel
"""    

def softbank_parser():
    #0. Paramters
    folder="D:\\02.Operator\\02.Softbank\\02.Operator Terminal Requirements\\OTR-2022.Q2.Q3\OTR-20210730_FullPackage\\02_Conformance_sheet\\"
    prefix="OTR-M2M|OTR-MTC" #regular expression
    
    #1. Get fileName in the folder
    fileName = file_operation.getFileNameList(folder, prefix)
    #2. Get each items in the files
    keyColumnName = ["Status", "Capability", "Requirement ID", "Function\n(Description)", "Reference\n(Section Name)", ]
    productType = ["M2M", "Manufacturer brand M2M"]
    sheetName="Conformance Sheet"
    itemMap = getItemsFromExcel(fileName, sheetName, keyColumnName, productType)
    #3. Output to one Excels
    outputFileName = "D:\\99.Source\\01.Python\\99.PythonStudy\\result\\softbank_item.xlsx"
    
    outputExcel(outputFileName, productType, itemMap)

if __name__ == '__main__':
    softbank_parser()