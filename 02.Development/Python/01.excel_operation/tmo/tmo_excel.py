import re
import openpyxl
from common import file_operation
from common import excel_operation

def getItemFromExcel(fileName, sheetName, keyMap, productType):
    
    excel = openpyxl.load_workbook(fileName)
    sheet = excel[sheetName]
    parser = excel_operation.ExcelParser(2, keyMap, 2, productType)
    parser.createMap(sheet)
    
    item = parser.parseExcel( fileName, 3, sheet)
    
    result = {}
    
    excel.close()
    return result

def tmo_parser():
    #0. Paramters
    folder = "D:\\02.Operator\\01.TMO\\2022_Q3\\"
    prefix = "T-MobileUS_MTR"
    #1. Get fileName in the folder
    fileName = file_operation.getFileNameList( folder, prefix )
    crFileName = ""
    mtrFileName = ""
    for f in fileName:
        if re.search("cr", f):
            crFileName = f
        else: mtrFileName = f
    
    #2. Get each items in the files
    sheetName = "MTR"
    keyColumnName = {
        "Id": "Global ID", 
        "Description":  "Description", 
        "Status": "Status", 
        "ChapterId":"Heading", 
        "Chapter": "Name", 
        "SectionId": "Heading", 
        "Section": "Name",
        "DocLocation":"TRD"
    }
    productType = [ "Priority",
                    "      High-Tier Smartphone"      ,
                    "      Mid-Tier Smartphone"       ,
                    "      Value Smartphone"          ,
                    "      Feature Phone"             ,
                    "      Tablet"                    ,
                    "      Mobile Hotspot/Router"     ,
                    "      Fixed Broadband: Router"   ,
                    "      Wearable"                  ,
                    "      Internet-of-Things"        ]
    #2.1 Get Critical Column
    item = getItemFromExcel(mtrFileName, sheetName, keyColumnName, productType)
    

if __name__ == '__main__':
    tmo_parser()