from django.db import models
from e_platform import EPlatformFwversion
from e_product import EProduct

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

class RPlatformFwversionFeature(models.Model):
    platform_version = models.OneToOneField(EPlatformFwversion, models.DO_NOTHING, db_column='platform_version', primary_key=True)
    platform = models.ForeignKey(EPlatformFwversion, models.DO_NOTHING)
    feature = models.ForeignKey(EFeature, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'r_platform_fwversion_feature'
        unique_together = (('platform_version', 'platform', 'feature'),)