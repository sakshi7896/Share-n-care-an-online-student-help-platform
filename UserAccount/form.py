import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from .models import Profile


class RegistrationForm(forms.Form):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
            (FRESHMAN, 'Freshman'),
            (SOPHOMORE, 'Sophomore'),
            (JUNIOR, 'Junior'),
            (SENIOR, 'Senior'),
    )
    username = forms.CharField(label='Username', max_length=30,widget=forms.TextInput(attrs={'required': True,'placeholder':'User Name','name':'username'}))
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'required': True,'placeholder':'Email Address'}))
    password = forms.CharField(label='Password',
                          widget=forms.PasswordInput())
    conf_password = forms.CharField(label='Password (Again)',
                        widget=forms.PasswordInput())
    mobile = forms.CharField(label='Mobile Number', max_length=10)

    year = forms.ChoiceField(choices=YEAR_IN_SCHOOL_CHOICES,widget=forms.Select())
    branch = forms.CharField(max_length=50)
    course = forms.CharField(max_length=7)

    class Meta:
       # model=RegistrationForm
        fields = ('username','email','password','confirm password','mobile','year','branch','course')
        #widgets={'name': TextInput(attrs={'class':'form-control', 'placeholder':'name'})}


    def clean_conf_password(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            conf_password = self.cleaned_data['conf_password']
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





   # def clean_year(self):

       # if 'year' in self.cleaned_data:
      #      year=self.cleaned_data['year']
        #    for in

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (username', 'password')
