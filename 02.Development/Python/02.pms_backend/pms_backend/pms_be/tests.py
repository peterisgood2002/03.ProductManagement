import sys
import unittest

from django.test import TestCase


from pms_be.views import getCNN5

# Create your tests here.

class CNNTest(TestCase):
    def test_getCNN5(self):
        print(sys.path)
        getCNN5()
        
        
