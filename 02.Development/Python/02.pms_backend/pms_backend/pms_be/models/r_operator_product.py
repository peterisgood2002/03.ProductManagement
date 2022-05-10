from django.db import models

from .e_operator import EOperator
from .e_product import EProduct

class ROpRfp(models.Model):
    operator = models.OneToOneField(EOperator, models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey(EProduct, models.DO_NOTHING)
    version_no = models.CharField(max_length=45)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_op_rfp'
        unique_together = (('operator', 'product', 'version_no'),)