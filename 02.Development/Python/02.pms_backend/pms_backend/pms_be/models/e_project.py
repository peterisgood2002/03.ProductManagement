from django.db import models

from .e_employee import EEmployee
from .e_customers import ECustomer

class EProject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, db_collation='utf8_general_ci', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    pm = models.ForeignKey(EEmployee, models.DO_NOTHING, db_column='pm', blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    alpha_project = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_project'

class RProjectCustomer(models.Model):
    customer = models.OneToOneField(ECustomer, models.DO_NOTHING, primary_key=True)
    project = models.ForeignKey(EProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'r_project_customer'
        unique_together = (('customer', 'project'),)


