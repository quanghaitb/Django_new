from django.shortcuts import render
from django.http import HttpResponse
from .models import postForm

# Create your views here.
def blog(request):
    pf = postForm.objects.all()
    return render(request, 'blog/blog.html', {'pf': pf})
def postBlog(request, id):
    pD = postForm.objects.get(id = id)
    return render(request, 'blog/postDetail.html', {'pD': pD})