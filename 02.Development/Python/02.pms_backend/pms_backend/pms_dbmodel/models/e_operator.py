from django.db import models

from .e_employee import EEmployee

class EArea(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_area'


class EOperator(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, db_collation='utf8mb3_general_ci', blank=True, null=True)
    area = models.ForeignKey(EArea, models.DO_NOTHING)
    url = models.TextField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_operator'



class EComplianceVersion(models.Model):
    version_no = models.CharField(primary_key=True, max_length=45)
    operator = models.ForeignKey('EOperator', models.DO_NOTHING)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    doc_url = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_compliance_version'
        unique_together = (('version_no', 'operator'),)

class VAreaOperator(models.Model):
    area = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    operator_id = models.IntegerField()
    operator = models.CharField(max_length=45, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'v_area_operator'
