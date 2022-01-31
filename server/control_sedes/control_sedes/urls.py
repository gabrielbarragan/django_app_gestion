"""control_sedes URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('organizations.urls')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('headquarters.urls')),
    path('api/v1/', include('timetables.urls')),

    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
]
