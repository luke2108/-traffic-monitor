from django.db import models

class UserError(models.Model):
    id = models.AutoField(primary_key=True)
    ip_user = models.CharField(max_length=100, null=True, blank=True)
    user_agent = models.CharField(max_length=10000, null=True, blank=True)
    domain = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ["-id"]
        db_table = "user_error"