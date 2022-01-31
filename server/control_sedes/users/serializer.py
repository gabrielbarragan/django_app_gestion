from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers


#my models
from users.models import Account
from headquarters.serializer import HeadQuarterSerializer

class AccountSerializer(serializers.ModelSerializer):
    """Serializer for users views"""
    
    class Meta:
        
        model= Account
        fields = ['id','first_name', 'last_name', 'email','username', 'password', 'address', 'phone', 'country', 'state', 'city','is_organization_admin']
        
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Account(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserSerializerAccess(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)
    headquarter = serializers.IntegerField(
        required=True)
    class Meta:
        model= Account
        fields=['email','username','headquarter', 'password']
        depth=1
class UserSerializerResponse(serializers.Serializer):
    access=serializers.BooleanField()
    headquarter = serializers.JSONField()
    depth=1
