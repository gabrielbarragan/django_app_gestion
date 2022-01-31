from rest_framework import serializers

#my models
from timetables.models import TimeTable

class TimeTableSerializer(serializers.ModelSerializer):
    """Serializers for Timetables views"""
    class Meta:
        model = TimeTable
        fields = '__all__'
