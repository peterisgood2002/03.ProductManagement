from datetime import date
from django.db import models
from pms_dbmodel.models.e_operator import EComplianceVersion
from pms_dbmodel.models.e_operator import EOperator
from pms_dbmodel.models.e_operator import EArea

# Create your models here.
def getArea(area) -> EArea:
    r = EArea.objects.get_or_create(name = area)
    if r[1] == True:
        r[0].create_date = date.today()
        r[0].update_date = date.today()
        r[0].save()
        
    return r[0]

class OperatorOperation:
    @classmethod
    def getOperator(cls, area, operator) -> EOperator:
        a = getArea(area)
        
        r = EOperator.objects.get_or_create(name = operator, area = a )
        if r[1] == True:
            r[0].create_date = date.today()
            r[0].update_date = date.today()
            r[0].save()
        
        return r[0]
    
    @classmethod
    def addVersion( cls, area, operator, version):
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
        