from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_Forms
from .models import contactForm
from django.views import View

# Create your views here.

class contact(View):
    
    def get(self, request):
        cf = contact_Forms
        return render(request, 'contact/contact.html', {'cf':cf})
   
    
    def post(self, request):
        if request.method  == 'POST':
            cf = contact_Forms(request.POST)
            if cf.is_valid():
                saveCF = contactForm(username = cf.cleaned_data['username'],
                                    email = cf.cleaned_data['email'], body  = cf.cleaned_data['body'] )
                saveCF.save()
                return HttpResponse('SAVED!')
            else:
                return HttpResponse('NOT METHOD POST')
        else: 
            return HttpResponse("ERROR")

# def contact(request):
#     cf = contact_Form
#     # context = { 'cf': contact_Form}
#     return render(request, 'contact/contact.html', {'cf': cf})
    
    
# def getContact(request):
#     if request.method == 'POST':
#         cf = contact_Form(request.POST)
#         if cf.is_valid:
#             cf.save()
#             return HttpResponse('Saved!')
#     else:
#         return HttpResponse('Method not POST')