from django.db import models
from .base import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=250, null=True, blank=False)
    body = models.TextField(null=True, blank=False, help_text='Article description')
    favourite_count = models.PositiveBigIntegerField(default=0, null=False, blank=False,
                                                     help_text='Number of favorite of an article')
