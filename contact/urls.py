from django.contrib import admin
from django.urls import path
from . import views
from django.views import View
app_name = 'contact'

urlpatterns = [
    path('', views.contact.as_view(), name = 'contact'),
    # path('saveContact/', views.saveContact, name = 'saveContact')
    # path('getContact', views.getContact, name = 'getContact')
]
