from django.db import models

from .e_employee import EEmployee

class ECustomer(models.Model):
    name = models.CharField(max_length=45, db_collation='utf8_general_ci', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    cpm = models.ForeignKey(EEmployee, models.DO_NOTHING, db_column='cpm', blank=True, null=True)
    is_alpha = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_customer'

