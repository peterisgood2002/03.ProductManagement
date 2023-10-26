from unittest import skip
from django.test import TestCase

# Create your tests here.
from contextlib import contextmanager
from django.test import TestCase
import pytest
from pms_dbmodel.models.e_operator import EComplianceVersion
from pms_dbmodel.models.e_operator import EOperator
from pms_dbmodel.operator_models import *
from pms_dbmodel.models.e_operator import EArea
from pms_dbmodel.models.e_employee import EEmployee
from pms_dbmodel.models.e_operator_requirement import (
    EDocStructureCategory,
    EDocStructure,
    EDeviceRequirement,
    EDeviceRequirementDesc,
)
from pms_dbmodel.models.a_attribute import APriority
from django.db import connection
from django.db import connections
from django.db import models
import logging


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


@pytest.mark.django_db
class EmployeeTest(PMSDbTest):
    def setUp(self):
        super().setManaged(EEmployee)

    def test_insertEmployee(self):
        e = EEmployee(id=1, english_name="test")

        e.save()
        teste = EEmployee.objects.get(id=1)
        print(teste)
        self.assertNotEqual(teste, None)


class OperatorOperationTest(PMSDbTest):
    logger = logging.getLogger("OperatorOperation")

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super().setManaged(
            EArea,
            EOperator,
            EComplianceVersion,
            EDocStructureCategory,
            EDocStructure,
            APriority,
            EDeviceRequirement,
            EDeviceRequirementDesc,
        )

    area = "NA"

    def testGetArea(self):
        self.logger.info("[testGetArea][BEGIN]")
        a = AreaOperation.getArea(self.area)
        self.assertIsInstance(a, EArea)
        assert a.name == self.area

        b = AreaOperation.getArea(self.area)
        assert a == b

        self.logger.info("[testGetArea][END]")

    operator1 = "ATT"
    operator2 = "TMO"

    def _checkOperator(self, operator, name):
        self.assertIsInstance(operator, EOperator)
        assert operator.name == name
        assert int(operator.id / 100) == operator.area.id
        assert operator.area.name == self.area

    def testGetOperator(self):
        self.logger.info("[testGetOperator][BEGIN]")
        # 1. Insert ATT
        o = OperatorOperation.addOperator(self.area, self.operator1)
        self._checkOperator(o, self.operator1)

        o = OperatorOperation.getOperator(self.operator1)
        self._checkOperator(o, self.operator1)
        assert self.operator1 == o.name
        o = OperatorOperation.getOperator(self.operator2)
        assert o == None

        # 2. Insert TMO
        tmo = OperatorOperation.addOperator(self.area, self.operator2)
        self._checkOperator(tmo, self.operator2)

        # 3. Get TMO again
        o = OperatorOperation.addOperator(self.area, self.operator2)
        assert tmo == o

        self.logger.info("[testGetOperator][END]")

    def _checkVersion(self, version: EComplianceVersion, operator, version_no):
        assert version.version_no == version_no
        self._checkOperator(version.operator, operator)

    def testGetVersions(self):
        self.logger.info("[testGetVersions][BEGIN]")
        r = VersionOperation.getVersions(self.area, self.operator1)
        assert 0 == len(r)

        [version, succeed] = VersionOperation.addVersion(
            self.area, self.operator1, "19.3"
        )
        self._checkVersion(version, self.operator1, "19.3")
        assert succeed == True
        [version, succeed] = VersionOperation.addVersion(
            self.area, self.operator1, "19.3"
        )
        self._checkVersion(version, self.operator1, "19.3")
        assert succeed == False
        [version, succeed] = VersionOperation.addVersion(
            self.area, self.operator1, "22.1"
        )
        self._checkVersion(version, self.operator1, "22.1")
        assert succeed == True

        r = VersionOperation.getVersions(self.area, self.operator1)
        assert 2 == len(r)
        assert "19.3" in r
        assert "22.1" in r

        r = VersionOperation.getVersion(self.operator1, "19.3")
        self._checkVersion(r, self.operator1, "19.3")

        self.logger.info("[testGetVersions][END]")

    def _checkDocStructure(
        self,
        data: EDocStructure,
        operator,
        verison,
        id,
        title,
        parent_id: EDocStructure,
    ):
        self._checkOperator(data.operator, operator)
        self._checkVersion(data.version, operator, verison)
        assert data.id == id
        assert data.name == title

        if parent_id != None:
            self.assertIsInstance(data.parent_structure, EDocStructure)
            data.parent_structure.id = parent_id.id

    categories = ["Document", "Chapter", "Section"]

    def _addCategories(self):
        for c in self.categories:
            category = DocOperation.addDocStructureCategory(c)
            assert category.name == c

    def testInsertChapterAndSection(self):
        self.logger.info("[testInsertChapterAndSection][BEGIN]")
        self._addCategories()

        version = "19.3"
        titleId = "1"
        title = "TEST"
        [chapter, succeed] = DocOperation.addDocStructure(
            self.area, self.operator1, version, self.categories[1], titleId, title
        )
        assert succeed == True

        chapter = DocOperation.getDocStructure(self.operator1, version, titleId)
        self._checkDocStructure(chapter, self.operator1, version, titleId, title, None)

        sectionId = "1.1"
        section = "TEST 1"
        [data, succeed] = DocOperation.addDocStructure(
            self.area,
            self.operator1,
            version,
            self.categories[2],
            sectionId,
            section,
            chapter,
        )
        assert succeed == True
        data = DocOperation.getDocStructure(self.operator1, version, sectionId)
        self._checkDocStructure(
            data, self.operator1, version, sectionId, section, chapter
        )
        self.logger.info("[testInsertChapterAndSection][END]")

    def testInsertDeviceRequirement(self):
        i = 0
