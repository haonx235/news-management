from django.db import models
from .base import BaseModel


class User(BaseModel):
    email = models.CharField(max_length=255, null=False, blank=False)
    username = models.CharField(max_length=255, null=False, blank=False)
    fullname = models.CharField(max_length=128, null=False, blank=False)
    password = models.TextField(null=False, blank=False)
