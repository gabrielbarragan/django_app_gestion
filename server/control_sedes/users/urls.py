from django.urls import path, include

from users import views

urlpatterns = [
    path('users/', views.CreateListUSer.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/headquarters/access/', views.UserAccess.as_view()),
    
]