from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(help_text='Created date')
    updated_at = models.DateTimeField(help_text='Updated date')

    objects = models.Manager()

    class Meta:
        abstract = True
