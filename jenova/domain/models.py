from django.db import models

class Domain(models.Model):
    name = models.CharField(max_length=256)
    client_id = models.BigIntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)    