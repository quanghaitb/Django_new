from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from .models import postReg
from .forms import LoginForm

from .forms import Reg_Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

class registerUser(View):
    
    def get(self, request, *args, **kwargs):
        reg = Reg_Form
        return render(request, 'UserMember/register.html', {'reg': reg})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            reg = Reg_Form(request.POST)
            if reg.is_valid():
                save_Reg = postReg(username = reg.cleaned_data['username'], password = reg.cleaned_data['password'], userID = reg.cleaned_data['userID'])
                save_Reg.save()
                return render(request,'UserMember/noitification_success.html')
            else:
                return HttpResponse('NOT METHOD POST!')
        else:
            return HttpResponse('Error!')
                
# Create your views here.
class loginUser(View):
    def get(self, request):
        lForm = LoginForm
        return render(request,'UserMember/login.html', {'lForm': lForm})
    def post(self,request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'home/base.html')
            else:
                return HttpResponse('Fail')
