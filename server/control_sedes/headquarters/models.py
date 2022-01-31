from django.db import models
from django.db.models.fields.related import ForeignKey

from organizations.models import Organization
from django.db.models.fields import EmailField
from timetables.models import TimeTable



class HeadQuarter (models.Model):
    '''
    Head Quarter model 
    '''
    ACTIVO = 'On'
    INACTIVO = 'Of'
    STATUS_CHOICES = [(ACTIVO, 'Activo'), (INACTIVO, 'Inactivo')]
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = EmailField(max_length=254)
    organization = ForeignKey(Organization, related_name='headquarter', on_delete=models.CASCADE) 
    geolocalization = models.CharField(max_length=255)
    state = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=ACTIVO,
    )
    time_tables = models.ManyToManyField(TimeTable, related_name='horarios', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
