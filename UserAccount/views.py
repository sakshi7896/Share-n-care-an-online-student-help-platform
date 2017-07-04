from django.shortcuts import render,redirect
from UserAccount.form import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import smtplib
from django.db import models

from UserAccount.form import SignUpForm
from UserAccount.models import Profile,Book
from django.contrib.auth.models import User


from django.core.mail import send_mail, BadHeaderError

def login_user(request):
    if request.method == "POST":
        mail = request.POST['username']
        password = request.POST['password']
        user_id=request.POST['id']
        user = authenticate(username=mail, password=password)
        if user is not None:
            #return HttpResponse("user is there")
            if user.is_active:
                request.session['id']=user_id
                return HttpResponse("hello")
            else:
                return HttpResponse("Bye")
        else:
            return render(request, 'UserAccount/login.html',{'error_message':"Invalid user details"})
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

            message = 'Greetings Sir, This is a test Email sent from the Django Project on Successful Registration.'
            from_email = 'sonalibansal.igdtuw@gmail.com'
            email_msg="Subject: {} \n\n{}".format(subject,message)
            smtp = smtplib.SMTP('smtp.gmail.com',587)
            smtp.starttls()
            smtp.login('SENDERS EMAIL','SENDERS PASSWORD')
            smtp.sendmail('SENDERS EMAIL',email,email_msg)
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



def new_book_post(request):
    if request.method=='POST':
        form=BookPostForm(request.POST,request.FILES)
        if form.is_valid():
            book = Book()
            book.user_book_id=request.session['id']
            book.book_pic = form.cleaned_data['image']
            book.book_title = request.POST["book_title"]
            book.subject = request.POST["subject"]
            book.author = request.POST["author"]
            book.pub_year = request.POST["pub_year"]
            book.pub_name = request.POST["pub_name"]
            book.book_cond = request.POST["book_cond"]
            book.negotiable = request.POST["negotiable"]
            book.save()
            return HttpResponse('New book post has been added')
        else:
            return HttpResponse(form.errors)
    

    BookForm =BookPostForm(None)
    return render(request, 'UserAccount/bookform.html', {'form' :BookForm})

        
    
