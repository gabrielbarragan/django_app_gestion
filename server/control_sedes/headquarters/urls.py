from django.urls import path, include

from headquarters import views

urlpatterns = [
    path('organizations/<int:organization>/headquarters/', views.CreateListHeadQuarters.as_view()),
    path('organizations/<int:organization>/headquarters/<int:pk>/', views.HeadQuarterDetail.as_view()),
    
]