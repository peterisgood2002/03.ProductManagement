from django.db import models

from .e_project import EProject
from .e_platform import EPlatform
from .e_milestone import EMilestone
from .e_product import EProduct
from .e_employee import EEmployee
from .a_attribute import APriority
       


class RProductSchedule(models.Model):
    product = models.OneToOneField(EProduct, models.DO_NOTHING, primary_key=True)
    milestone = models.ForeignKey(EMilestone, models.DO_NOTHING)
    milestone_category = models.ForeignKey(EMilestone, models.DO_NOTHING, db_column='milestone_category', to_field='category_id')
    plan_start_dt = models.DateField(blank=True, null=True)
    plan_end_dt = models.DateField(blank=True, null=True)
    actual_start_dt = models.DateField(blank=True, null=True)
    actual_end_dt = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_product_schedule'
        unique_together = (('product', 'milestone', 'milestone_category'),)

class RProjectSchedule(models.Model):
    project = models.OneToOneField(EProject, models.DO_NOTHING, primary_key=True)
    milestone = models.ForeignKey(EMilestone, models.DO_NOTHING)
    milestone_category = models.ForeignKey(EMilestone, models.DO_NOTHING, db_column='milestone_category', to_field='category_id')
    plan_start_dt = models.DateField(blank=True, null=True)
    plan_end_dt = models.DateField(blank=True, null=True)
    actual_start_dt = models.DateField(blank=True, null=True)
    actual_end_dt = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_project_schedule'
        unique_together = (('project', 'milestone', 'milestone_category'),)

class EAction(models.Model):
    project = models.ForeignKey('RProjectSchedule', models.DO_NOTHING)
    milestone = models.ForeignKey('RProjectSchedule', models.DO_NOTHING, to_field='milestone_id')
    milestone_category = models.ForeignKey('RProjectSchedule', models.DO_NOTHING, db_column='milestone_category', to_field='milestone_category')
    action_id = models.IntegerField(primary_key=True)
    action_desc = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('EEmployee', models.DO_NOTHING)
    deadline = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    priority = models.ForeignKey(APriority, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_action'


