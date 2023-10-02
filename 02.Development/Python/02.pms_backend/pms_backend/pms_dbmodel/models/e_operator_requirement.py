from django.db import models

from .a_attribute import APriority

class EDocStructureCategory(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_doc_structure_category'


class EDocStructure(models.Model):
    #id = CompositeKey(columns=['operator', 'version', 'docId' ])
    operator = models.ForeignKey('EOperator', models.DO_NOTHING, db_column = 'operator_id', to_field= 'id')
    version = models.ForeignKey('EComplianceVersion', models.DO_NOTHING, db_column = 'version_no', to_field= 'version_no')
    id = models.CharField(max_length=45, db_collation='utf8mb3_general_ci', primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    category = models.ForeignKey(EDocStructureCategory, models.DO_NOTHING, db_column='category', blank=True, null=True)
    parent_structure = models.ForeignKey('EDocStructure', models.DO_NOTHING, to_field='id', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_doc_structure'
        unique_together = (('operator', 'version', 'id'),)



class EDeviceRequirement(models.Model):
    #id = CompositeKey(columns=['operator', 'version', 'docId' ])
    operator = models.ForeignKey('EOperator', models.DO_NOTHING, db_column = 'operator_id', to_field= 'id')
    version = models.ForeignKey('EComplianceVersion', models.DO_NOTHING, db_column = 'version_no', to_field= 'version_no')
    descId = models.ForeignKey('EDeviceRequirementDesc', models.DO_NOTHING)
    priority = models.ForeignKey(APriority, models.DO_NOTHING, db_column='priority', blank=True, null=True)
    structure = models.ForeignKey('EDocStructure', models.DO_NOTHING, to_field='id')
    tag_id = models.CharField(max_length=45, db_collation='utf8mb3_general_ci', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_device_requirement'
        unique_together = (('operator', 'version', 'descId'),)


class EDeviceRequirementDesc(models.Model):
    title = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    name = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    doc_loc = models.CharField(max_length=255, db_collation='utf8mb3_general_ci', blank=True, null=True)
    note = models.CharField(max_length=2048, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_device_requirement_desc'


class ERequirementCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_requirement_category'

        
class RDeviceRequirementCategory(models.Model):
    requirement = models.ForeignKey(EDeviceRequirement, models.DO_NOTHING)
    category = models.ForeignKey(ERequirementCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'r_device_requirement_category'
        unique_together = (('requirement', 'category'),)
