from django.db import models
from django.contrib.auth.hashers import make_password
from .base import BaseModel


class User(BaseModel):
    email = models.CharField(max_length=255, null=False, blank=False, unique=True)
    username = models.CharField(max_length=255, null=False, blank=False, unique=True)
    fullname = models.CharField(max_length=128, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        email = email or ""
        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email = email_name + "@" + domain_part.lower()
        return email

    def save(self, *args, **kwargs):
        self.email = self.normalize_email(self.email)
        if self.password is not None:
            raw_password = self.password
            self.password = make_password(raw_password)
        super(User, self).save(*args, **kwargs)
