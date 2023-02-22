from django.db import models

from .e_employee import EEmployee
from .a_attribute import ACategory
from .e_operator_ta import ETechnicalAcceptance

class EPlatformFamily(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    create_date = models.DateField(db_column='create_Date', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_platform_family'


class EPlatform(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, db_collation='utf8mb3_general_ci', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    ppm = models.ForeignKey(EEmployee, models.DO_NOTHING, db_column='ppm', blank=True, null=True)
    platform_family = models.ForeignKey('EPlatformFamily', models.DO_NOTHING)
    code_name = models.CharField(max_length=45, blank=True, null=True)
    category = models.ForeignKey(ACategory, models.DO_NOTHING, db_column='category')

    class Meta:
        managed = False
        db_table = 'e_platform'
        




