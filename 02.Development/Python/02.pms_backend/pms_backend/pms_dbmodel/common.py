from datetime import date
from django.db import models
import logging
from enum import Enum
from abc import abstractmethod


def setDateAndSave(data):
    if isinstance(data, tuple):
        if data[1] == True:
            data[0].create_date = date.today()
            data[0].update_date = date.today()
        else:
            data[0].update_date = date.today()
        data[0].save()
    elif isinstance(data, models.Model):
        data.update_date = date.today()
        data.save()


class LOGTIME(Enum):
    BEGIN = 0
    MIDDLE = 1
    END = 2


def logInfo(logger: logging.Logger, timing: LOGTIME, name, msg="", *args, **kwargs):
    data = "[%s][%s] %s" % (name, timing.name, msg)
    logger.info(data, *args, **kwargs)


class ArrayDate:
    def __init__(self, requirement=None):
        infoLen = self.getInfoLength()
        if len(requirement) <= infoLen:
            self._requirement = []
            for r in requirement:
                self._requirement.append(r)

            remaining = infoLen - len(requirement)
            for i in range(remaining):
                self._requirement.append(None)

    def getInfo(self, info: Enum):
        return self._requirement[info.value]

    @abstractmethod
    def getInfoLength(self):
        pass
