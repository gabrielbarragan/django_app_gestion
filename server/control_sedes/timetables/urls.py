from django.urls import path, include

from timetables import views

urlpatterns = [
    path('timetables/', views.CreateListTimeTables.as_view()),
    path('timetables/<int:pk>', views.TimeTableDetail.as_view()),
]