from django.db import models

from .e_operator import EComplianceVersion, EOperator

class ETestPlan(models.Model):
    operator = models.OneToOneField(EOperator, models.DO_NOTHING, primary_key=True)
    version_no = models.ForeignKey(EComplianceVersion, models.DO_NOTHING, db_column='version_no')
    test_id = models.IntegerField()
    title = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    test_description = models.CharField(max_length=2048, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_test_plan'
        unique_together = (('operator', 'version_no', 'test_id'),)