from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class CustomUser(AbstractUser):
    verified = models.IntegerField(blank=True, null=True)
    activated = models.BooleanField(blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateField( default = datetime.date.today)
    date_modified = models.DateField( default = datetime.date.today)

    def __str__(self):
        return self.email
