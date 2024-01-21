from django.db import models

from .e_project import EProject
from .e_platform import EPlatform
from .e_milestone import EMilestone
from .e_product import EProduct
from .e_employee import EEmployee
from .a_attribute import APriority
from .e_operator import EOperator


class RProductSchedule(models.Model):
    product = models.OneToOneField(
        EProduct, models.DO_NOTHING, primary_key=True
    )  # The composite primary key (product_id, milestone_id) found, that is not supported. The first column is selected.
    milestone = models.ForeignKey(EMilestone, models.DO_NOTHING)
    plan_start_dt = models.DateField(blank=True, null=True)
    plan_end_dt = models.DateField(blank=True, null=True)
    actual_start_dt = models.DateField(blank=True, null=True)
    actual_end_dt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "r_product_schedule"
        unique_together = (("product", "milestone"),)


class RProjectSchedule(models.Model):
    project = models.OneToOneField(
        EProject, models.DO_NOTHING, primary_key=True
    )  # The composite primary key (project_id, milestone_id, schedule_id) found, that is not supported. The first column is selected.
    milestone = models.ForeignKey(EMilestone, models.DO_NOTHING)
    schedule_id = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    plan_start_dt = models.DateField(blank=True, null=True)
    plan_end_dt = models.DateField(blank=True, null=True)
    actual_start_dt = models.DateField(blank=True, null=True)
    actual_end_dt = models.DateField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "r_project_schedule"
        unique_together = (("project", "milestone", "schedule_id"),)


class ROperatorSchedule(models.Model):
    operator = models.OneToOneField(
        EOperator, models.DO_NOTHING, primary_key=True
    )  # The composite primary key (operator_id, milestone_id) found, that is not supported. The first column is selected.
    milestone = models.ForeignKey(
        EMilestone,
        models.DO_NOTHING,
        db_comment="Operator has its own schedule to release document",
    )
    version = models.CharField(max_length=45, blank=True, null=True)
    plan_release_date = models.DateField(blank=True, null=True)
    actual_release_date = models.DateField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "r_operator_schedule"
        unique_together = (("operator", "milestone"),)


class EAction(models.Model):
    project = models.ForeignKey("RProjectSchedule", models.DO_NOTHING)
    milestone = models.ForeignKey(
        "RProjectSchedule", models.DO_NOTHING, to_field="milestone_id"
    )
    milestone_category = models.ForeignKey(
        "RProjectSchedule",
        models.DO_NOTHING,
        db_column="milestone_category",
        to_field="milestone_category",
    )
    action_id = models.IntegerField(primary_key=True)
    action_desc = models.TextField(blank=True, null=True)
    owner = models.ForeignKey("EEmployee", models.DO_NOTHING)
    deadline = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    priority = models.ForeignKey(APriority, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "e_action"
