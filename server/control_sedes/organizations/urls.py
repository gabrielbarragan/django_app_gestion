from django.urls import path, include

from organizations import views

urlpatterns = [
    path('organizations/', views.CreateListOrganization.as_view()),
    path('organizations/<int:pk>/', views.OrganizationDetail.as_view()),
]