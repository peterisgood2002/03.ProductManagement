from django.db import models

from .a_attribute import APriority

class EDocStructureCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_doc_structure_category'


class EDocStructure(models.Model):
    operator = models.OneToOneField('self', models.DO_NOTHING, primary_key=True)
    version_no = models.ForeignKey('self', models.DO_NOTHING, db_column='version_no', to_field='version_no')
    id = models.CharField(max_length=45, db_collation='utf8mb3_general_ci')
    name = models.CharField(max_length=45, blank=True, null=True)
    category = models.ForeignKey('EDocStructureCategory', models.DO_NOTHING, db_column='category')
    parent_structure = models.ForeignKey('self', models.DO_NOTHING, to_field='id')
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_doc_structure'
        unique_together = (('operator', 'version_no', 'id'),)



class EDeviceRequirement(models.Model):
    operator = models.OneToOneField('EDocStructure', models.DO_NOTHING, primary_key=True)
    version_no = models.ForeignKey('EDocStructure', models.DO_NOTHING, db_column='version_no', to_field='version_no')
    desc = models.ForeignKey('EDeviceRequirementDesc', models.DO_NOTHING)
    priority = models.ForeignKey(APriority, models.DO_NOTHING, db_column='priority', blank=True, null=True)
    structure = models.ForeignKey('EDocStructure', models.DO_NOTHING, to_field='id')
    tag_id = models.CharField(max_length=45, db_collation='utf8mb3_general_ci', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_device_requirement'
        unique_together = (('operator', 'version_no', 'desc'),)


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
    requirement_operator = models.OneToOneField(EDeviceRequirement, models.DO_NOTHING, primary_key=True)
    requirement_version_no = models.ForeignKey(EDeviceRequirement, models.DO_NOTHING, db_column='requirement_version_no', to_field='version_no')
    requirement = models.ForeignKey(EDeviceRequirement, models.DO_NOTHING, to_field='desc_id')
    category = models.ForeignKey(ERequirementCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'r_device_requirement_category'
        unique_together = (('requirement_operator', 'requirement_version_no', 'requirement', 'category'),)
