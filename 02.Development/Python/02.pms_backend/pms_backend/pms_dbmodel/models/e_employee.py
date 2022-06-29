from django.db import models

class EEmployee(models.Model):
    id = models.CharField(primary_key=True, max_length=10, db_collation='utf8_general_ci')
    chinese_name = models.CharField(max_length=45, db_collation='utf8_general_ci', blank=True, null=True)
    english_name = models.CharField(max_length=255, blank=True, null=True)
    nt_account = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_employee'
        