from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(help_text='Created date', auto_now_add=True)
    updated_at = models.DateTimeField(help_text='Updated date', auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True
