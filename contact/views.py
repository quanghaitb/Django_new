from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_Form

# Create your views here.
def contact(request):
    cf = contact_Form
    # context = { 'cf': contact_Form}
    return render(request, 'contact/contact.html', {'cf': cf})
    # return render(request, 'contact/contact.html')
def getContact(request):
    if request.method == 'POST':
        cf = contact_Form(request.POST)
        if cf.is_valid:
            cf.save()
            return HttpResponse('Saved!')
    else:
        return HttpResponse('Method not POST')