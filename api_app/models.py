from django.db import models


class DogsModel(models.Model):
    default_value = models.IntegerField(default=0)
    description = models.CharField(max_length=25)
    imgsrc = models.TextField(default='')


class SomeKeys(models.Model):
    default_value = models.IntegerField(default=0)
    name = models.TextField(default='')
