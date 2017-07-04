from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
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
    year = models.CharField(max_length=2,
            choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,)
    branch = models.CharField(max_length=50)
    course = models.CharField(max_length=10)


class Book(models.Model):
    user_book_id = models.ForeignKey(Profile,default=2)
    book_title = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pub_year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    pub_name = models.CharField(max_length=50)
    NEW='New'
    OLD='Old'
    CONDITION =(
        (NEW, 'New'),
        (OLD, 'Old'),
    )
    book_cond = models.CharField(max_length=3,
            choices=CONDITION,
        default=OLD,)
    book_pic = models.ImageField(upload_to='BookImages',default='BookImages/default_pic.png')
    YES='Y'
    NO='N'
    NEGOTIABILITY =(
        (YES, 'Yes'),
        (NO, 'No'),
    )
    negotiable = models.CharField(max_length=3,
            choices=NEGOTIABILITY,
        default=NO,)






