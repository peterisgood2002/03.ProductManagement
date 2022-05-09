from django.db import models

class ETechnicalAcceptance(models.Model):
    id = models.IntegerField(primary_key=True)
    issue_date = models.DateField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_technical_acceptance'