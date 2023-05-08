from django.shortcuts import render
from .models import categories
from .forms import LoginForm

from django.http import HttpResponse
from .forms import Reg_Form
# Create your views here.
class categories(View):
    def get(self, request):
        cate_all = categories.objects.all()
        lForm = LoginForm
        reg = Reg_Form
        return render(request, 'home/base.html',  {'lForm': lForm, 'reg': reg,'cate_all': cate_all})
    def getCategoryById(request, id):
        pD = categories.objects.get(id = id)
        return HttpResponse('By ID')