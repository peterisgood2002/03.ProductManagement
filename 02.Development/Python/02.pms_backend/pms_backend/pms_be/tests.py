import sys
import unittest

from django.test import TestCase


from pms_be.views import getCNN5
from pms_be.views import testCRREST
from pms_be.models.e_employee import EEmployee
# Create your tests here.

class CNNTest(TestCase):
    def test_getCNN5(self):
        getCNN5()

    def test(self):
        testCRREST()       
        
        