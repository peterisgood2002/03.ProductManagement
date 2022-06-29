from contextlib import contextmanager
from django.test import TestCase
from pms_dbmodel.models.e_employee import EEmployee
from django.db import connection
from django.db import connections
from django.db import models
# Create your tests here.
class PMSDbTest(TestCase):
    db_name = 'pms_db'
    databases = {'default', db_name}
    
    @contextmanager
    def setManaged( self, model: models.Model):
        with connections[self.db_name].schema_editor() as schema_editor:
            in_atomic_block = schema_editor.connection.in_atomic_block
            schema_editor.connection.in_atomic_block = False
            schema_editor.create_model(model)
            
            schema_editor.connection.in_atomic_block = in_atomic_block
            if (
                model._meta.db_table
                not in connections[self.db_name].introspection.table_names()
            ):
                raise ValueError(
                    "Table `{table_name}` is missing in test database.".format(
                        table_name=model._meta.db_table
                    )
                )  
    
    
class EmployeeTest(PMSDbTest):
    
    def setUp(self):
        super().setManaged(EEmployee)
        
    def test_insertEmployee(self):
        e = EEmployee( id = 1, english_name = "test")
        e.save()
        teste = EEmployee.objects.get(id = 1)
        print(teste)
        self.assertNotEqual(teste, None)