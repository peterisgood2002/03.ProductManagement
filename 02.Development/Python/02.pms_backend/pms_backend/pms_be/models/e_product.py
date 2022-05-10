from django.db import models

from .a_attribute import ACategory
from .e_operator_ta import ETechnicalAcceptance


class EProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, db_collation='utf8_general_ci', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(ACategory, models.DO_NOTHING)
    ta = models.ForeignKey(ETechnicalAcceptance, models.DO_NOTHING, blank=True, null=True)
    forecast_qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_product'
