from django.db.models.query import QuerySet
from datetime import date
from django.db import models


class CommonOperation:
    @staticmethod
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

    @staticmethod
    def getIndex(id, data: QuerySet):
        result = id
        if len(data) != 0:
            result = data[0].id + 1
        return result

    @staticmethod
    def searchWithName(name, model: models.Model) -> models.Model:
        rList = model.objects.filter(name=name)

        if len(rList) == 0:
            return None

        return rList[0]
