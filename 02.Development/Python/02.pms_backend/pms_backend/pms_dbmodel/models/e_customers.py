from django.db import models

from .e_employee import EEmployee
from .e_area import EArea


class ECustomer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(
        max_length=45, db_collation="utf8mb3_general_ci", blank=True, null=True
    )
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    cpm = models.ForeignKey(
        "EEmployee", models.DO_NOTHING, db_column="cpm", blank=True, null=True
    )
    is_alpha = models.IntegerField()
    area = models.ForeignKey(EArea, models.DO_NOTHING, db_column="area")

    class Meta:
        managed = False
        db_table = "e_customer"
