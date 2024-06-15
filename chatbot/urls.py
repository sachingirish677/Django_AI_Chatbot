from django.urls import path
from . import views

urlpatterns = [
    path('' , views.chatbot, name='chatbot'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/register/', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]