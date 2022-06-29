from django.test import TestCase

from pms_operator.operator.att_excel import att_excel_parser


class ATTTest(TestCase):
    def _testReadOnlyItems(self):
        data = att_excel_parser("D:\\02.Operator\\01.AT&T\\04.FeatureRequirements_13289.Compliance Metrix\\v19.3\\13289 19.3.xlsx",19.3, True)
        
        self.assertIsInstance(data, dict)
        self.assertEqual(1, len(data) ) 
        
    def testReadItemsAndChange(self):
        data = att_excel_parser("D:\\02.Operator\\01.AT&T\\04.FeatureRequirements_13289.Compliance Metrix\\v19.3\\13289 19.3.xlsx",19.3, False)
        
        self.assertIsInstance(data, dict)    
        self.assertEqual(4, len(data) ) 
        