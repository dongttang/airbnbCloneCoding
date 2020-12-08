from django.db import models


class AbstractTimeStampModel(models.Model):
    class Meta:
        abstract = True

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
