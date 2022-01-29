from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import EmailField
from phonenumber_field.modelfields import PhoneNumberField

#my models


class Organization (models.Model):
    '''
    Organization model 
    '''
    admin_user = ForeignKey('users.Account', related_name='organization_admin',on_delete=models.CASCADE)
    nit = models.BigIntegerField()
    name = models.CharField(max_length=255)
    comercial_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = PhoneNumberField(null=False)
    email = EmailField(max_length=254)
    website = models.URLField(max_length=200, blank=True)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
