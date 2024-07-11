from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout
from crm_admin.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

def register_view(request):
    return render(request,'Register.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        if password == confirm_password:
            hashed_password = make_password(password)  # Hash the password
            user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
            user.save()
            print(user.email)
            return HttpResponse('Data submitted successfully!')
        else:
            return HttpResponse('Passwords do not match!')
    else:
        return HttpResponse('Invalid request method.')
    
    
def login_view(request):
    return render(request,'login.html')

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user = authenticate(email=email, password=password)
        if user is not None:
            # login(request, user)  # Log the user in
            # return HttpResponse('Login successful!')
            return render(request,'addcourses.html')
            
        else:
            return HttpResponse('Invalid credentials.')
    else:
        return HttpResponse('Invalid request method.')        
        
# @login_required   
# def coursesData(request):
#     return render(request,"addcourses.html")
