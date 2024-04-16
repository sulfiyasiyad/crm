from django.db import models


# Create your models here.
class card(models.Model):
    name=models.CharField(max_length=255)
    status=models.PositiveIntegerField(default=0)
