import logging
from enum import Enum
from abc import abstractmethod


class LOGTIME(Enum):
    BEGIN = 0
    MIDDLE = 1
    END = 2


def logInfo(logger: logging.Logger, timing: LOGTIME, name, msg="", *args, **kwargs):
    data = "[%s][%s] %s" % (name, timing.name, msg)
    logger.info(data, *args, **kwargs)


class ArrayData:
    def __init__(self, data=None):
        infoLen = self.getInfoLength()
        if len(data) <= infoLen:
            self._data = []
            for r in data:
                self._data.append(r)

            remaining = infoLen - len(data)
            for i in range(remaining):
                self._data.append(None)

    def getInfo(self, info: Enum):
        return self._data[info.value]

    @abstractmethod
    def getInfoLength(self):
        pass

    def getData(self):
        return self._data
