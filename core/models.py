from django.db import models

# Create your models here.


class AbstractTimeStampModel(models.Model):
    class Meta:
        abstract = True

    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
