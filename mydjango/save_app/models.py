# Create your models here.

from django.db import models


class My_save_model(models.Model):
    con1 = models.CharField(max_length=255)
    con2 = models.CharField(max_length=255)
