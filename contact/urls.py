from django.contrib import admin
from django.urls import path
from . import views
app_name = 'contact'

urlpatterns = [
    path('', views.contact, name = 'contact'),
    path('saveContact/', views.saveContact, name = 'saveContact')
    # path('getContact', views.getContact, name = 'getContact')
]
