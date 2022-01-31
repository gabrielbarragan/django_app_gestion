from django.shortcuts import render

from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_202_ACCEPTED

from headquarters.permisions import HeadQuarterPermission

from headquarters.models import HeadQuarter
from users.models import Account

from headquarters.serializer import HeadQuarterSerializer

# Create your views here.
class HeadQuarterDetail(generics.RetrieveAPIView):
    """View detail of a headquarters"""

    queryset = HeadQuarter.objects.all()
    serializer_class = HeadQuarterSerializer

class CreateListHeadQuarters(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    """View for create and list headquarters"""

    serializer_class = HeadQuarterSerializer
    queryset = HeadQuarter.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



    