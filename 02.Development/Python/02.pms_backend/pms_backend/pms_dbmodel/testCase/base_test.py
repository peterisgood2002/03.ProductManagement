from unittest import skip
from django.test import TestCase
from django.db import connection
from django.db import connections
import logging

from pms_dbmodel.common import logInfo, LOGTIME

logger = logging.getLogger(__name__)


# Create your tests here.
class PMSDbTest(TestCase):
    db_name = "pms_db"
    databases = {"default", db_name}

    @classmethod
    def setManaged(self, *model):
        schema_editor = connections[self.db_name].schema_editor()
        in_atomic_block = schema_editor.connection.in_atomic_block
        with schema_editor:
            schema_editor.connection.in_atomic_block = False
            for m in model:
                if (
                    m._meta.db_table
                    not in connections[self.db_name].introspection.table_names()
                ):
                    schema_editor.create_model(m)

        schema_editor.connection.in_atomic_block = in_atomic_block

    def setUp(self) -> None:
        logInfo(logger, LOGTIME.BEGIN, self._testMethodName)
        return super().setUp()

    def tearDown(self) -> None:
        logInfo(logger, LOGTIME.END, self._testMethodName)
        return super().tearDown()
