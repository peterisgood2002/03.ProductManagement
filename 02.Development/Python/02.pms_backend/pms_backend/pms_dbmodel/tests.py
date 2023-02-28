from unittest import skip
from django.test import TestCase

# Create your tests here.
from contextlib import contextmanager
from django.test import TestCase
from pms_dbmodel.models.e_operator import EComplianceVersion
from pms_dbmodel.models.e_operator import EOperator
from pms_dbmodel.operator_models import OperatorOperation
from pms_dbmodel.models.e_operator import EArea
from pms_dbmodel.models.e_employee import EEmployee
from django.db import connection
from django.db import connections
from django.db import models
# Create your tests here.
class PMSDbTest(TestCase):
    db_name = 'pms_db'
    databases = {'default', db_name}
    
    @classmethod
    def setManaged( self, *model):
        
        schema_editor = connections[self.db_name].schema_editor()
        in_atomic_block = schema_editor.connection.in_atomic_block
        with  schema_editor:
            schema_editor.connection.in_atomic_block = False
            for m in model:
                schema_editor.create_model(m)
                schema_editor
                if (
                    m._meta.db_table
                    not in connections[self.db_name].introspection.table_names()
                ):
                    raise ValueError(
                        "Table `{table_name}` is missing in test database.".format(
                            table_name=model._meta.db_table
                        )
                    )  
        
        schema_editor.connection.in_atomic_block = in_atomic_block
           
    
    
class EmployeeTest(PMSDbTest):
    
    def setUp(self):
        super().setManaged(EEmployee)
        
    def test_insertEmployee(self):
        e = EEmployee( id = 1, english_name = "test")
        
        e.save()
        teste = EEmployee.objects.get(id = 1)
        print(teste)
        self.assertNotEqual(teste, None)

    
class OperatorOperationTest(PMSDbTest):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(EArea, EOperator, EComplianceVersion)
    
    area = 'NA'
    
    def testGetArea(self):
        a = OperatorOperation.getArea(self.area)
        self.assertIsInstance(a, EArea)
        self.assertEqual(a.name, self.area)

        b = OperatorOperation.getArea(self.area)
        self.assertEqual(a, b)

    operator1 = 'ATT'
    operator2 = 'TMO'
    def testGetOperator(self):
        #1. Insert ATT
        o = OperatorOperation.getOperator(self.area, self.operator1)
        self.assertIsInstance(o, EOperator)
        self.assertEqual(o.name, self.operator1 )
        self.assertEqual(o.area.name, self.area)
        
        #2. Insert TMO
        tmo = OperatorOperation.getOperator(self.area, self.operator2)
        self.assertEqual(tmo.name, self.operator2 )
        self.assertEqual(tmo.area.name, self.area)
        
        #3. Get TMO again
        o = OperatorOperation.getOperator(self.area, self.operator2)
        self.assertEqual(tmo, o)

    def testGetVersions(self):
        r = OperatorOperation.getVersions(self.area, self.operator1)
        self.assertEqual(0, len(r) )
        
        suceed = OperatorOperation.addVersion(self.area, self.operator1, '19.3')
        self.assertTrue(suceed)
        suceed = OperatorOperation.addVersion(self.area, self.operator1, '22.1')
        self.assertTrue(suceed)
        r = OperatorOperation.getVersions(self.area, self.operator1)
        self.assertEqual(2, len(r) )
        self.assertIn('19.3', r)
        self.assertIn('22.1', r)
        
        

    def test_insertEmployee(self):
        e = EEmployee( id = 1, english_name = "test")
        e.save()
        teste = EEmployee.objects.get(id = 1)
        print(teste)
        self.assertNotEqual(teste, None)