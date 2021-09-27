
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'Homepage/index.html')


def flight(request):
    return render(request, 'Homepage/searchflight.html')


def detail(request):
    return render(request, 'Homepage/detail.html')


def contact(request):
    return render(request, 'Homepage/contact.html')


def login(request):
    return render(request, 'Homepage/loginpage.html')


def signup(request):
    return render(request, 'Homepage/signup.html')
