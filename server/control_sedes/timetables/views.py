#rest_frameworks imports
from rest_framework import generics
from rest_framework import mixins

#model imports
from timetables.models import TimeTable

#serielizers imports
from timetables.serializer import TimeTableSerializer

# Create your views here.
class CreateListTimeTables(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """View for create and list TimeTables"""
    serializer_class = TimeTableSerializer
    queryset = TimeTable.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TimeTableDetail(generics.RetrieveAPIView):
    """View for detail of Timetables"""
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer