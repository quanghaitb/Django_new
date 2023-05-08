from django.shortcuts import render
from django.http import HttpResponse
from UserMember.forms import LoginForm
from django.views import View
from UserMember.forms import Reg_Form

# Create your views here.

def index(request):
    lForm = LoginForm
    reg = Reg_Form
    return render(request, 'home/index.html',  {'lForm': lForm, 'reg': reg})