from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime
from PIL import Image

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
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    user_book = models.ForeignKey(Profile,null=False)

    book_title = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    

    pub_year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    pub_name = models.CharField(max_length=50)
    price=models.CharField(max_length=5,null=True)
    NEW='New'
    OLD='Old'
    CONDITION =(
        (NEW, 'New'),
        (OLD, 'Old'),
    )
    book_cond = models.CharField(max_length=3,
            choices=CONDITION,
        default=OLD,)
    

    book_pic=models.ImageField(upload_to='BookImages',blank=True)

    YES='Y'
    NO='N'
    NEGOTIABILITY =(
        (YES, 'Yes'),
        (NO, 'No'),
    )
    SELL='S'
    DONATE='D'
    Type=(
        (SELL,'S'),
        (DONATE,'D'),
        )
    b_type=models.CharField(max_length=1,choices=Type,default=SELL)
    negotiable = models.CharField(max_length=3,
            choices=NEGOTIABILITY,
        default=NO,)
    created_time=models.DateTimeField(auto_now_add = True)

class Counselling(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
		
		#name = models.CharField(max_length=50)
	name1 = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	college = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=10)
	branch = models.CharField(max_length=50)
	PLACEMENT = 'PL'
	CAREER = 'CA'
	EDUCATION = 'ED'
	PSYCHOLOGY = 'PS'
	COUNSELLING_CHOICES = (
	    (PLACEMENT, 'Placement'),
	    (CAREER, 'Career'),
	    (EDUCATION, 'Education'),
	    (PSYCHOLOGY, 'Psychology'),
	)
	c_choices = models.CharField(max_length=2,
	        choices=COUNSELLING_CHOICES,
	    default=CAREER,)
	    
	description = models.CharField(max_length=1000)
	URGENT = 'UR'
	WAIT = 'WA'
	STATUS_CHOICES = (
	    (URGENT, 'Urgent'),
	    (WAIT, 'Wait'),
	)
	status_c = models.CharField(max_length=2,
	        choices=STATUS_CHOICES,
	    default=WAIT,)

		
    
    


