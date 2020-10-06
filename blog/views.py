from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'blog/blog_home.html', {})

def contact(request):
    return render(request, 'contact/contact.html', {})

def bloglist(request):
    return render(request, 'blog/blog.html', {})

def blogpost(request):
    return render(request, 'blog/blogpost.html', {})

def about(request):
    return render(request, 'about.html', {})

def login(request):
    return render(request, 'auth/login.html', {})

def register(request):
    return render(request, 'auth/register.html', {})
