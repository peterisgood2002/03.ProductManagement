from datetime import date
from django.db import models

from pms_dbmodel.models.e_operator import EComplianceVersion
from pms_dbmodel.models.e_operator import EOperator
from pms_dbmodel.models.e_operator import EArea
from pms_dbmodel.models.e_operator_requirement import EDocStructureCategory, EDocStructure
import logging

class OperatorRequirement:
   def __init__(self, Id, title, description, chapterId, chapter, sectionId, section):
       self._id = Id
       self._title = title
       self._description = description
       self._chapterId = chapterId
       self._sectionId = sectionId
       self._section = section
    

# Create your models here.
class OperatorOperation:
   
    logger = logging.getLogger("OperatorOperation")
    @classmethod
    def _setDate( cls, data ):
        if data[1] == True:
            data[0].create_date = date.today()
            data[0].update_date = date.today()
            data[0].save()
        else:
            data[0].update_date = date.today()
            data[0].save()
    
    @classmethod
    def getArea(cls, area) -> EArea:
        r = EArea.objects.get_or_create(name = area)
        cls._setDate(r)
        
        return r[0]

    @classmethod
    def getOperator(cls, area, operator) -> EOperator:
        cls.logger.info("[getOperator][BEGIN] AREA = %s, Operator = %s", area, operator )
        a:EArea = cls.getArea(area)
        operators = EOperator.objects.filter(area = a).order_by('-id')
        
        result = None
        
        for o in operators:
            if o.name == operator:
               result = o
        
        if result == None:
            index = a.id * 100
            if len( operators ) != 0:
                index = operators[0].id + 1
            r = EOperator.objects.get_or_create(id = index, name = operator, area = a )
            result = r[0]
        cls.logger.info("[getOperator][END] Result = %d", result.id )
        return result
    
    @classmethod
    def _addVersion( cls, area, operator, version):
        o = cls.getOperator(area, operator)
        
        result = EComplianceVersion.objects.get_or_create(operator = o, version_no = version)
        cls._setDate(result)
        
        return result
    
    @classmethod
    def addVersion( cls, area, operator, version):
        
        v = cls._addVersion(area, operator, version)
        cls.logger.info("[addVersion][END] AREA = %s, Operator = %s, Version = %s, Insert/Update(True/False) = %s", area, operator, version, v[1] )

        return v[1]
        
    
    @classmethod
    def getVersions( cls, area, operator):
        #1. check whether this operator is the first one
        o = cls.getOperator(area, operator)
        #2. get the versions for this operator
        versions = EComplianceVersion.objects.filter( operator = o)
        
        r = []
        for v in versions:
            r.append( v.version_no)
            
        return r
    
    @classmethod
    def getVersion( cls, area, operator, version):
        cls.logger.info("[getVersion][BEGIN] AREA = %s, Operator = %s, Version = %s", area, operator, version )
        
        v = cls._addVersion(area, operator, version)
        
        return v[0]

    @classmethod
    def addDocStructureCategory(cls, category) -> EDocStructureCategory:
        cls.logger.info("[addDocStructureCategory][BEGIN] Category = %s", category )
        r = EDocStructureCategory.objects.get_or_create(name = category)
        
        cls._setDate(r)
        
        return r[0]
    
    @classmethod
    def getDocStructureCategory(cls, category):
        r = EDocStructureCategory.objects.get_or_create(name = category)
        cls._setDate(r)
        
        return r[0]
    
    @classmethod
    def addDocStructure(cls, area, operator, version, category, id, title):
        cls.logger.info("[getVersion][BEGIN] AREA = %s, Operator = %s, Version = %s, Id = %s", area, operator, version, id )
        version = cls.getVersion(area, operator, version )
        cate = cls.getDocStructureCategory(category)
        r = EDocStructure.objects.get_or_create(operator = version.operator, version = version, category = cate, id = id)
        
        cls._setDate(r)

        