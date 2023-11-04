# Create your tests here.
from contextlib import contextmanager
from django.test import TestCase
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

from django.db import models
