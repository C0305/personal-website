from django.db import models
from cobosio.constants import COUNTRIES
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class Company(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=2000, blank=True, null=True)
    sub_domain = models.CharField(max_length=30)
    user_limit = models.IntegerField(default=5)
    country = models.CharField(max_length=3, choices=COUNTRIES, blank=True, null=True)



