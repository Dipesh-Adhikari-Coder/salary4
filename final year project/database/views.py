from django.shortcuts import render, redirect
from . import views
from django.contrib.auth.models import User
from django.contrib import messages
from finalyearproj import settings
from django.shortcuts import render, redirect
from .model import Registeredusers
from Registeredusers.models import Registeredusers
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    form = UserCreationForm()

    if request.method == "POST":

        if  request.POST.get('username') and request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('pass1'):
           
            
            username = request.POST.get('username')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            password = request.POST.get('pass1')
            
            
            
            newuser = User.objects.create_user(username=username, firstname=firstname, lastname=lastname, email=email, password=password)
            newuser.save()
  
            messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
            
            
            
            return render(request, 'Homepage/signup.html')

    else:
        return render(request, 'Homepage/index.html')
        
        