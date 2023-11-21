from django.db import models

from .e_project import EProject
from .e_platform import EPlatform
from .e_product import EProduct
from viewflow.fields import CompositeKey


class RProjectPlatform(models.Model):
    id = CompositeKey(columns=["project", "platform"])
    project = models.ForeignKey(
        EProject, models.DO_NOTHING, db_column="project_id", to_field="id"
    )  # The composite primary key (project_id, platform_id) found, that is not supported. The first column is selected.
    platform = models.ForeignKey(
        EPlatform, models.DO_NOTHING, db_column="platform_id", to_field="id"
    )
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "r_project_platform"
        unique_together = (("project", "platform"),)


class RProjectTargetProduct(models.Model):
    project = models.OneToOneField(EProject, models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey(EProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "r_project_target_product"
        unique_together = (("project", "product"),)
