from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=256)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)