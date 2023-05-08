from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from .models import postReg
from .forms import LoginForm

from .forms import Reg_Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class registerUser(View):
    
    def get(self, request, *args, **kwargs):
        reg = Reg_Form
        return render(request, 'UserMember/register.html', {'reg': reg})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            reg = Reg_Form(request.POST)
            if reg.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                passwordConfirm = request.POST.get('password2')
                userID = request.POST.get('userID')
                if password != passwordConfirm:
                    return HttpResponse("Password not match!")
                else:
                    
                    save_Reg = postReg(username = reg.cleaned_data['username'], password = reg.cleaned_data['password'], userID = reg.cleaned_data['userID'])
                    save_Reg.save()
                    user = authenticate(request, username = reg.cleaned_data['username'], password = reg.cleaned_data['password'])
                    
                    if user is not None:
                        if user.is_active:
                            login(request, user)
                            return render(request, 'home/base.html', {'user': user})
                    else:
                        return HttpResponse('ERRROR')
        else:
            return HttpResponse('Error!')
                
# Create your views here.
class loginUser(View):
    def get(self, request):
        lForm = LoginForm
        reg = Reg_Form
        return render(request,'UserMember/base.html', {'lForm': lForm,'reg': reg})
    def post(self,request):
        lForm = LoginForm
        reg = Reg_Form
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'home/base.html', {'user': user,'lForm': lForm,'reg': reg})
                    
            else:
                return HttpResponse('Fail')

def logoutUser(request):
    logout(request)
    lForm = LoginForm
    reg = Reg_Form
    return render(request, 'home/base.html',{'lForm': lForm, 'reg':reg})