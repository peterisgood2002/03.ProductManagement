from django.db import models
from .e_product import EProduct
from .e_project import EProject
from .e_operator_ta import ETechnicalAcceptance

class EFeature(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_feature'
        
class RProductFeature(models.Model):
    product = models.OneToOneField(EProduct, models.DO_NOTHING, primary_key=True)
    feature = models.ForeignKey(EFeature, models.DO_NOTHING)
    parameters = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_product_feature'
        unique_together = (('product', 'feature'),)

class EProjectFwversion(models.Model):
    project = models.OneToOneField(EProject, models.DO_NOTHING, primary_key=True)
    version = models.CharField(max_length=255, db_collation='utf8_general_ci')
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    ta = models.ForeignKey(ETechnicalAcceptance, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_project_fwversion'
        unique_together = (('project', 'version'),)
