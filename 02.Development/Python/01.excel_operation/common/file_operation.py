from os import listdir
from os.path import isfile, join
import re
"""
getFileNameList
"""
def getFileNameList( folder, prefix ):

    fileName = []
    for f in listdir( folder ):
        if isfile(join(folder, f)) :
            s = re.search(prefix, f)
            if s and s.start() == 0:
                fileName.append(folder + f)
    return fileName
"""
End getFileNameList
"""
