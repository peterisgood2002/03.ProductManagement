
from django.test import TestCase

from pms_dbmodel.models.e_operator import EArea, EOperator



class ItemTest(TestCase):
    
    def setUp(self) -> None:
        area = EArea.objects.create( name = "NA")
        EOperator.objects.create(name = "ATT", area = area)
        
        return super().setUp() 
    
    def testGetOperator(self):
        #data = EOperator.objects.get(name = "ATT")
        
        i = 0
        