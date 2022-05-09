from django.db import models

from e_employee import EEmployee

class EArea(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_area'

class EOperator(models.Model):
    name = models.CharField(max_length=45, db_collation='utf8_general_ci', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    spm = models.ForeignKey(EEmployee, models.DO_NOTHING, db_column='spm', blank=True, null=True)
    area = models.ForeignKey(EArea, models.DO_NOTHING)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_operator'

class EComplianceVersion(models.Model):
    version_no = models.CharField(primary_key=True, max_length=45)
    operator = models.ForeignKey(EOperator, models.DO_NOTHING)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    doc_url = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_compliance_version'
        unique_together = (('version_no', 'operator'),)


