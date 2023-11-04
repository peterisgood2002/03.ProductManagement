from datetime import date
from django.db import models


from pms_dbmodel.common import *
import logging


class OperatorRequirement:
    def __init__(self, Id, title, description, chapterId, chapter, sectionId, section):
        self._id = Id
        self._title = title
        self._description = description
        self._chapterId = chapterId
        self._chapter = chapter
        self._sectionId = sectionId
        self._section = section

    def getChapterId(self):
        return self._chapterId

    def getSectionId(self):
        return self._sectionId


logger = logging.getLogger(__name__)
