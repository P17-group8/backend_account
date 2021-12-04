from django.db import models

class Plaza(models.Model):
    id     = models.BigAutoField(primary_key=True)
    isAvailable = models.BooleanField(default=True)