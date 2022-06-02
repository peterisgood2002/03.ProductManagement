from django.test import TestCase

from pms_operator.operator.att_excel import att_excel_parser


class ATTTest(TestCase):
    def test(self):
        
        att_excel_parser("D:\\02.Operator\\01.AT&T\\04.FeatureRequirements_13289.Compliance Metrix\\v19.3\\13289 19.3.xlsx",19.3)