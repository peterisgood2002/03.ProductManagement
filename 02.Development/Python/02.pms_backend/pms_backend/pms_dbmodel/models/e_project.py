from django.db import models

from .e_employee import EEmployee
from .e_customers import ECustomer
from .a_attribute import ACategory, APriority
from viewflow.fields import CompositeKey


class EProject(models.Model):
    name = models.CharField(
        max_length=45, db_collation="utf8mb3_general_ci", blank=True, null=True
    )
    alpha_project = models.IntegerField(blank=True, null=True)
    priority = models.ForeignKey(
        APriority, models.DO_NOTHING, db_column="priority", blank=True, null=True
    )
    note = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "e_project"


class RProjectCustomer(models.Model):
    id = CompositeKey(columns=["customer", "project"])
    customer = models.ForeignKey(
        ECustomer, models.DO_NOTHING, db_column="customer_id", to_field="id"
    )  # The composite primary key (customer_id, project_id) found, that is not supported. The first column is selected.
    project = models.ForeignKey(
        EProject, models.DO_NOTHING, db_column="project_id", to_field="id"
    )
    relationship = models.ForeignKey(
        ACategory, models.DO_NOTHING, db_column="relationship"
    )
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "r_project_customer"
        unique_together = (("customer", "project"),)
