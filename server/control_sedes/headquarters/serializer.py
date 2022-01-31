from dataclasses import fields
from rest_framework import serializers

#my models
from headquarters.models import HeadQuarter
from users.models import Account
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model= Account
        fields=['headquarter']

class HeadQuarterSerializer(serializers.ModelSerializer):
    """Serializers for headquarters views"""
    
    class Meta:
        model = HeadQuarter
        fields= '__all__'
        

     

