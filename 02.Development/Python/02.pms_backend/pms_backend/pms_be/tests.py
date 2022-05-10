import sys
import unittest

from django.test import TestCase

#from pms_be.views import testView
from pms_be.models.e_employee import EEmployee
# Create your tests here.
class EmployeeTest(TestCase):
    
    def test_insertEmployee(self):
        e = EEmployee( id = 1, english_name = "test")
        e.save()
        teste = EEmployee.objects.get(id = 1)
        print(teste)
        self.assertNotEqual(teste, None)
        
        