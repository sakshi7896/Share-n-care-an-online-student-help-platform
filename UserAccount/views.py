from django.shortcuts import render,redirect
from UserAccount.form import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import smtplib
from django.db import models
from django import template
from django.template.loader import get_template
from UserAccount.form import SignUpForm
from UserAccount.models import Profile,Book
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect

from django.http import JsonResponse
from django.core import serializers
from django.core.mail import send_mail, BadHeaderError
import pprint
import datetime

from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import update_session_auth_hash


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'UserAccount/home.html')

def writetous(request):
    return render(request, 'UserAccount/contactus.html')

def search_view(request):
    return render(request, 'UserAccount/search.html')

def login_user(request):
    if request.method == "POST":
        mail = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=mail, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                request.session['id'] = user.id
                return render(request, 'UserAccount/home.html')
            else:
                return HttpResponse("Inactive User")
        else:
            return render(request, 'UserAccount/login.html',{'error_message':"Invalid user Credentials"})
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
            subject = 'Registration Successful- Share And Care'

            message = 'Greetings! Ypu have been successfully registered on Share And Care - An Online Student Help Platform. We are very happy to welcome you on BOARD with us!'
            from_email = 'sharencare@hotmail.com'
            email_msg="Subject: {} \n\n{}".format(subject,message)
            smtp = smtplib.SMTP('smtp.live.com',25)
            smtp.starttls()
            smtp.login('senders email','senders password')
            smtp.sendmail('senders email',email,email_msg)
            smtp.quit()
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

def search_book(request):
    if not request.user.is_authenticated:
        return render(request, 'UserAccount/login.html')
    if request.method == "POST":
        q = request.POST['query']
        option = request.POST['option']
        if(option=='Name'):
            try:
                queryset = Book.objects.filter(book_title__icontains=q)
            except Book.DoesNotExist:
                return HttpResponse("No results found")
            context = {
            'queryset':queryset,
            'q':q,
            }
            return render(request, 'UserAccount/search_results.html', context)
        elif(option=='Subject'):
            try:
                queryset=Book.objects.filter(subject__icontains=q)
            except Book.DoesNotExist:
                return HttpResponse("No results found")
            context = {
            'queryset':queryset,
            'q':q,
            }
            return render(request, 'UserAccount/search_results.html', context)
            

def new_book_post(request):
    if request.method=='POST':
        form=BookPostForm(request.POST,request.FILES)
        if form.is_valid():
            book = Book()
            user = User.objects.get(id=request.session['id'])
            profile = Profile.objects.get(user=user)
            book.user_book=profile
            book.book_pic = form.cleaned_data['image']
            book.book_title = request.POST["book_title"]
            book.subject = request.POST["subject"]
            book.author = request.POST["author"]
            book.pub_year = request.POST["pub_year"]
            book.pub_name = request.POST["pub_name"]
            book.book_cond = request.POST["book_cond"]
            book.negotiable = request.POST["negotiable"]
            book.price = request.POST["price"]
            book.b_type = 'S'
            book.save()
            return HttpResponse('New book post has been added')
        else:
            return HttpResponse(form.errors)
    

    BookForm =BookPostForm(None)
    return render(request, 'UserAccount/bookform.html', {'form' :BookForm})
	
def donate_book_post(request):
    if request.method=='POST':
        form=BookDonateForm(request.POST,request.FILES)
        if form.is_valid():
            book = Book()
            user = User.objects.get(id=request.session['id'])
            profile = Profile.objects.get(user=user)
            book.user_book=profile
            book.book_pic = form.cleaned_data['image']
            book.book_title = request.POST["book_title"]
            book.subject = request.POST["subject"]
            book.author = request.POST["author"]
            book.pub_year = request.POST["pub_year"]
            book.pub_name = request.POST["pub_name"]
            book.book_cond = request.POST["book_cond"]
            book.b_type = 'D'
            book.negotiable = 'N'
            book.price = 0.0
            book.save()
            return HttpResponse('New book for donation has been added')
        else:
            return HttpResponse(form.errors)
    

    donateBookForm =BookDonateForm(None)
    return render(request, 'UserAccount/donatebookform.html', {'form' :donateBookForm})

	
def counselling_post(request):
    if request.method=='POST':
        form=CounsellingForm(request.POST,request.FILES)
        if form.is_valid():
            counselling = Counselling()
            user = User.objects.get(id=request.session['id'])
            profile = Profile.objects.get(user=user)
            book.user_book=profile
            book.book_pic = form.cleaned_data['image']
            book.book_title = request.POST["book_title"]
            book.subject = request.POST["subject"]
            book.author = request.POST["author"]
            book.pub_year = request.POST["pub_year"]
            book.pub_name = request.POST["pub_name"]
            book.book_cond = request.POST["book_cond"]
            book.b_type = 'D'
            book.negotiable = 'N'
            book.price = 0.0
            book.save()
            return HttpResponse('New book for donation has been added')
        else:
            return HttpResponse(form.errors)
    

    donateBookForm =BookDonateForm(None)
    return render(request, 'UserAccount/counsellingform.html', {'form' :donateBookForm}) #to chancge

def change_password(request):
    message = " "
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if not request.user.is_authenticated:
            return redirect('login_user')
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('view_profile')
        else:
            message = "Either Old Password Incorrect or New Passwords do not match"
            context={
            'form':form,
            'error_message':message
            }
            return render(request,'UserAccount/change_password.html',context)
    form = PasswordChangeForm(request.user, request.POST)
    return render(request, 'UserAccount/change_password.html',{'form': form})


def view_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.session['id'])
        userprofile = Profile.objects.get(user=user)
        context = {
        'userprofile':userprofile,
                }
        return render(request, 'UserAccount/view_profile.html', context)
    else:
        return render(request, 'UserAccount/login.html')



def recent(request):
    #results=Book.objects.all().order_by('-created_time')[:2]
    results=Book.objects.all()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(results)
    posts_serialized = serializers.serialize('json', results)
    pp.pprint(posts_serialized)
    return JsonResponse(posts_serialized, safe=False) 
    
