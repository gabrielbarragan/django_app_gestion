from django.shortcuts import render

from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser
from organizations.models import Organization

from organizations.serializer import OrganizationSerializer

# Create your views here.
class OrganizationDetail(generics.RetrieveAPIView):
    """View for details of an organization"""
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class CreateListOrganization(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """View for create and list organizations"""
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

