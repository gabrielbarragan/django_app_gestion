from tabnanny import verbose
from django.db import models


DAYS_OF_WEEK = (
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),
    )
class Days(models.Model):

    day = models.CharField(max_length=10,choices= DAYS_OF_WEEK)
    class Meta:
        ordering = ('-day',)
    
    def __str__(self):
        return self.day

class TimeTable (models.Model):
    '''
    TimeTable model 
    '''
    days = models.ManyToManyField('Days')
    head_quarter = models.ManyToManyField('headquarters.HeadQuarter', related_name='sede', blank=True) 
    
    start_time = models.TimeField()
    end_time = models.TimeField()
    class Meta:
        ordering = ('start_time',)
    
    def __str__(self):
        name = 'timetable'+str(self.pk)
        return name
