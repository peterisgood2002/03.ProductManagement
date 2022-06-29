import sys
import unittest

from django.test import TestCase


from pms_be.views import getCNN5
from pms_be.views import testCRREST

# Create your tests here.

class CNNTest(TestCase):
    def test_getCNN5(self):
        print(sys.path)
        getCNN5()

    def test(self):
        testCRREST()       
        
        