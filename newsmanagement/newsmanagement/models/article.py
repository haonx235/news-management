from django.db import models
from .base import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=250, null=False, blank=True)
    body = models.TextField(null=False, blank=True)
    favourite_count = models.PositiveBigIntegerField(default=0, null=False, blank=False)
