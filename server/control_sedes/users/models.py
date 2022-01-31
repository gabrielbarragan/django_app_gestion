
import email
from enum import unique
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.related import ForeignKey


#field types models
from phonenumber_field.modelfields import PhoneNumberField

#my models
from organizations.models import Organization
from headquarters.models import HeadQuarter
from timetables.models import TimeTable

# Create your models here.

class Account(AbstractUser):
    """Model User Account for users of organization"""
    email = models.EmailField(max_length=254, verbose_name='email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    organization = ForeignKey(Organization, related_name='account',on_delete=models.CASCADE,blank=True, null=True)
    headquarter = models.ManyToManyField(HeadQuarter, related_name='account')
    timetables = models.ManyToManyField(TimeTable, blank=True)
    address = models.CharField(max_length=255)
    phone = PhoneNumberField(null=False)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    modified = models.DateTimeField(auto_now=True)
    is_organization_admin = models.BooleanField(default=False)

    class Meta:
        ordering = ('-modified',)

    def __str__(self):

        """Return username"""
        return self.username

