from django.db import models
from e_operator_requirement import EDeviceRequirement
from a_attribute import ACompliance
from e_operator_testplan import ETestPlan
from e_operator_ta import ETechnicalAcceptance
from e_operator_requirement import EDeviceRequirement

class RTaComplyDeviceRequirement(models.Model):
    operator = models.OneToOneField(EDeviceRequirement, models.DO_NOTHING, primary_key=True)
    version_no = models.ForeignKey(EDeviceRequirement, models.DO_NOTHING, db_column='version_no')
    requirement = models.ForeignKey(EDeviceRequirement, models.DO_NOTHING)
    technical_acceptance = models.ForeignKey(ETechnicalAcceptance, models.DO_NOTHING)
    compliance = models.ForeignKey(ACompliance, models.DO_NOTHING, db_column='compliance')

    class Meta:
        managed = False
        db_table = 'r_ta_comply_device_requirement'
        unique_together = (('operator', 'version_no', 'requirement', 'technical_acceptance'),)


class RTaComplyTestPlan(models.Model):
    technical_acceptance = models.OneToOneField(ETechnicalAcceptance, models.DO_NOTHING, primary_key=True)
    test = models.ForeignKey(ETestPlan, models.DO_NOTHING)
    version_no = models.ForeignKey(ETestPlan, models.DO_NOTHING, db_column='version_no')
    operator = models.ForeignKey(ETestPlan, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'r_ta_comply_test_plan'
        unique_together = (('technical_acceptance', 'test', 'version_no', 'operator'),)

class RTestPlanExamineDeviceRequirement(models.Model):
    operator = models.OneToOneField(ETestPlan, models.DO_NOTHING, primary_key=True)
    version_no = models.ForeignKey(ETestPlan, models.DO_NOTHING, db_column='version_no')
    requirement = models.ForeignKey(EDeviceRequirement, models.DO_NOTHING)
    test = models.ForeignKey(ETestPlan, models.DO_NOTHING)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_test_plan_examine_device_requirement'
        unique_together = (('operator', 'version_no', 'requirement', 'test'),)