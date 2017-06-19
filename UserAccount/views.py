from django.shortcuts import render,redirect
#from django.contrib.auth.form import UserCreationForm
from UserAccount.form import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'UserAccount/login.html')

def index(request):
    return HttpResponse("<h2> HEY! </h2>")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password'],email=form.cleaned_data['email'],mobile=form.cleaned_data['mobile'],year=form.cleaned_data['year'],branch=form.cleaned_data['branch'],course=form.cleaned_data['course'])
            return HttpResponseRedirect('/')
    form = RegistrationForm()
    #variables = RequestContext(request, {'form': form})
    return render(request,'UserAccount/register.html',{'form': form})
    
