from django.db import models
from .a_attribute import ACategory


class EMilestone(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(ACategory, models.DO_NOTHING)
    milestone_name = models.TextField(blank=True, null=True)
    deliverable = models.TextField(blank=True, null=True)
    parent_milestone = models.ForeignKey(
        "self",
        models.DO_NOTHING,
        db_column="parent_milestone",
        blank=True,
        null=True,
    )
    estimated_baseline = models.ForeignKey(
        ACategory,
        models.DO_NOTHING,
        db_column="estimated_baseline",
        related_name="emilestone_estimated_baseline_set",
        blank=True,
        null=True,
    )

    estimated = models.FloatField(blank=True, null=True)

    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "e_milestone"
