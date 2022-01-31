from django.contrib import admin
from timetables.models import TimeTable, Days

# Register your models here.
admin.site.register(TimeTable)
admin.site.register(Days)