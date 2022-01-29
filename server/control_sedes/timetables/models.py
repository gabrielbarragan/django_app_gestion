from django.db import models


class TimeTable (models.Model):
    '''
    TimeTable model 
    '''
    head_quarter = models.ManyToManyField('headquarters.HeadQuarter', related_name='sede') 
    start_time = models.TimeField()
    end_time = models.TimeField()
    class Meta:
        ordering = ('start_time',)
    
    def __str__(self):
        return self.head_quarter.name