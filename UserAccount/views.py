from django.shortcuts import render,redirect
from UserAccount.form import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from django.db import models

from UserAccount.form import SignUpForm
from UserAccount.models import Profile
from django.contrib.auth.models import User



def login_user(request):
    if request.method == "POST":
        mail = request.POST['username']
        password = request.POST['password']
        #return HttpResponse(password)

        user = authenticate(username=mail, password=password)
        if user is not None:
            #return HttpResponse("user is there")
            if user.is_active:
                return HttpResponse("hello")
            else:
                return HttpResponse("Bye")
        else:
            return render(request, 'UserAccount/login.html',{'error_message':"Invlid user details"})
    return render(request, 'UserAccount/login.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            username = request.POST.get('username')
            email =request.POST.get('email')
            password = request.POST.get('password1')
            phone_number=request.POST.get('phone_number')
            year=request.POST.get('year')
            branch=request.POST.get('branch')
            course=request.POST.get('course')
            
            
            p1=User(username=username,email=email,password=password)
            p1.set_password(password)
            p1.save()
            newUser=Profile(user=p1,phone_number=phone_number,year=year,branch=branch,course=course)
            newUser.save()


            
            return HttpResponse('<h2>registration successful</h2>')
        else:
            form = SignUpForm()
            context={
            'form':form,
            'error_message':"Invalid User details"
            }
            return render(request, 'UserAccount/register.html',context)

    form = SignUpForm()
    return render(request, 'UserAccount/register.html',{'form': form})
