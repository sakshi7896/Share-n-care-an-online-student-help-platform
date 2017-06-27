
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from .models import Profile


class SignUpForm(forms.ModelForm):

    username = forms.CharField(label='Username', max_length=30,widget=forms.TextInput(attrs={'required': True,'placeholder':'User Name','name':'username'}))
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'required': True,'placeholder':'Email Address'}))
    
    password1= forms.CharField(label='Password',
                          widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)',
                        widget=forms.PasswordInput())
    
   
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password1', 'password2','phone_number','year','branch','course' )
       

        
    def clean_conf_password(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password1']
            conf_password = self.cleaned_data['password2']
            if password == conf_password:
                return conf_password
        raise forms.ValidationError('Passwords do not match.')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')

   


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']
