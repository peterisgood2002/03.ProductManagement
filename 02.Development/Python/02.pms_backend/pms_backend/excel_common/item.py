from enum import Enum

"""
  Class Items
"""


class Item:
    def __init__(self, fileName, keyInfo: Enum):
        self.fileName = fileName
        self.keyValueList = []

        self.setKeyInfo(keyInfo)

    def setKeyInfo(self, keyInfo: Enum):
        self._keyInfo = keyInfo

    def getKetInfo(self):
        return self._keyInfo

    def setKey(self, key: Enum, value):
        self.keyValueList[key.value] = value

    def getKey(self, key: Enum):
        value = self.keyValueList[key.value]
        return value
