from django.db import models


class ACategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category_name = models.CharField(
        max_length=45, db_collation="utf8mb3_general_ci", blank=True, null=True
    )
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "a_category"


class ACompliance(models.Model):
    compliance_id = models.IntegerField(primary_key=True)
    compliance_name = models.CharField(max_length=45, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    compliance_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "a_compliance"


class APriority(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "a_priority"
