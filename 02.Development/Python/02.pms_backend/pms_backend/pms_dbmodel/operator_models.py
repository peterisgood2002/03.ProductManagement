from datetime import date
from django.db import models

from pms_dbmodel.models.e_operator import EComplianceVersion
from pms_dbmodel.models.e_operator import EOperator
from pms_dbmodel.models.e_operator import EArea
import logging


# Create your models here.
class OperatorOperation:
   
    logger = logging.getLogger("OperatorOperation")
    @classmethod
    def getArea(cls, area) -> EArea:
        r = EArea.objects.get_or_create(name = area)
        if r[1] == True:
            r[0].create_date = date.today()
            r[0].update_date = date.today()
            r[0].save()
        
        
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
    def addVersion( cls, area, operator, version):
        cls.logger.info("[addVersion][BEGIN] AREA = %s, Operator = %s, Version = %s", area, operator, version )
        o = cls.getOperator(area, operator)
        
        v = EComplianceVersion.objects.get_or_create(operator = o, version_no = version)
        if v[1] == True:
            v[0].create_date = date.today()
            v[0].update_date = date.today()
            v[0].save()
        
        else:
            return False
            
        return True
        
    
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
        