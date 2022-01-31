from rest_framework import serializers

#my models
from organizations.models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    """Serializers for Organizations views"""
    class Meta:
        model = Organization
        fields = '__all__'

