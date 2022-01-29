from django.db import models
from django.db.models.fields.related import ForeignKey

class TimeTable (models.Model):
    '''
    TimeTable model 
    '''

    head_quarter = ForeignKey('headquarters.HeadQuarter', related_name='sede',on_delete=models.CASCADE) 
    start_time = models.TimeField()
    end_time = models.TimeField()
    user= ForeignKey('users.Account', related_name='user_time',on_delete=models.CASCADE)
    class Meta:
        ordering = ('start_time',)
    
    def __str__(self):
        return self.head_quarter.name