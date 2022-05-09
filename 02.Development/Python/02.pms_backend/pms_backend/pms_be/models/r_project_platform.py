from django.db import models

from e_project import EProject
from e_platform import EPlatform
from e_product import EProduct

class RProjectPlatform(models.Model):
    project = models.OneToOneField(EProject, models.DO_NOTHING, primary_key=True)
    platform = models.ForeignKey(EPlatform, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'r_project_platform'
        unique_together = (('project', 'platform'),)

class RProjectTargetProduct(models.Model):
    project = models.OneToOneField(EProject, models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey(EProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'r_project_target_product'
        unique_together = (('project', 'product'),)