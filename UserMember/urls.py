from django.contrib import admin 
from django.urls import path 
from . import views
from django.views import View
app_name = 'UserMember'

urlpatterns = [
    path('register', views.registerUser.as_view(), name= 'register'),
    path('login', views.loginUser.as_view(), name= 'login'),
    path('logout', views.logoutUser, name= 'logout')
]