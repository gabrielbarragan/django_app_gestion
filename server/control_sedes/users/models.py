import email
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey

from phonenumber_field.modelfields import PhoneNumberField

#my models
from organizations.models import Organization

# Create your models here.

class Account(models.Model):
    """proxy model that extense the information of user model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = ForeignKey(Organization, related_name='organization',on_delete=models.CASCADE)
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
        return self.user.username

