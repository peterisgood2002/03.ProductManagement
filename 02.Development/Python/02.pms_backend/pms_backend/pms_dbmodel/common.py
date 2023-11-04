from datetime import date
from django.db import models
import logging
from enum import Enum


def setDateAndSave(data: tuple[models.Model, bool]):
    if data[1] == True:
        data[0].create_date = date.today()
        data[0].update_date = date.today()
    else:
        data[0].update_date = date.today()
    data[0].save()


class LOGTIME(Enum):
    BEGIN = 0
    MIDDLE = 1
    END = 2


def logInfo(logger: logging.Logger, timing: LOGTIME, name, msg="", *args, **kwargs):
    data = "[%s][%s] %s" % (name, timing.name, msg)
    logger.info(data, *args, **kwargs)
