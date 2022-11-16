from datetime import datetime
from email.policy import default
from random import choices
from shutil import register_unpack_format
from tabnanny import verbose
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractBaseUser):
    first_name=models.CharField(max_length=100, null=True,verbose_name="first_name")
    middle_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="middle name")
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="last name")
    email = models.EmailField(_('email address'), unique=True)
    date_joined =models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(blank=True,  verbose_name="groups", to='auth.Group', related_name="user_set", related_query_name="user")
    user_permissions = models.ManyToManyField(blank=True, verbose_name="user_permissions", to='auth.Permission', related_name="user_set", related_query_name="user")

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

    objects =CustomUserManager()
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
            return self.is_superuser

    def has_module_perms(self, app_label):
            return self.is_superuser

    

class Application(models.Model):
    TITTLE = (
        ('Ms', 'Ms'),
        ('Mrs','Mrs'),
        ('Mr','Mr'),
    )

    COURSES = (
        ('Computer  Engineering', 'Computer Engineering'),
        ('Information Technology Management', 'Information Technology Management'), 
        ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'),
        ('Electronics Engineering', 'Electronics Engineering'),
    )
    CAMPUS =(
        ('Main Campus','Main Campus'),
        ('Kisumu Town Campus', 'Kisumu Town Campus'),
        ('Town Campus CBD', 'Town Campus CBD'),
        ('Marsabit Town Campus', 'Marsabit Town Campus'),
    )
 
    COHORT =(
        ('January Cohort', 'January Cohort'),
        ('May Cohort', 'May Cohort'),
        ('September Cohort', 'September Cohort'),
    )

    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )


 
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(choices= TITTLE, null= True ,max_length=10)
    surname = models.CharField(max_length=200) 
    email = models.EmailField(CustomUser, null= True ) 
    phone_no = models.IntegerField(max_length=10, null=True) 
    date_of_birth = models.DateField(null=True)
    id_number =models.IntegerField(max_length=10, null=True)
    date_joined=models.DateField(default=timezone.now)
    address = models.TextField(max_length=200) 
    postal_code = models.IntegerField(null=True)
    city = models.CharField(null=True ,max_length=10)
    country = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)
    course = models.CharField(max_length=100, choices= COURSES)
    campus=models.CharField(choices=CAMPUS, null=True,max_length=70)
    cohort=models.CharField(choices=COHORT, null=True ,max_length=80)
    birth_certificate = models.ImageField(upload_to="docs", null=True)
    leaving_certificate = models.ImageField(upload_to="docs", null=True)
    Application_Status = models.TextField(max_length=100, choices=STATUS, default="Pending")
    message = models.TextField(max_length=100, default="")
 
    def __str__(self):
        return self.email

class Profile(models.Model):
    GENDER =(
        ('Male','Male' ), ('Female', 'Female'), ('Other', 'Other'),
    )

    DISABILITY =(
        ('YES', 'YES'), ('NO', 'NO')
    )

    MARITAL_STATUS = (
        ('Single', 'Single'), 
        ('Married', 'Married') ,
        ('Engaged','Engaged'), 
        ('Complicated', 'Complicated'),
        ('Separated', 'Separated'),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender = models.CharField(choices =GENDER,max_length=100 )
    disability = models.TextField(choices=DISABILITY)
    marita_status =models.TextField(choices=MARITAL_STATUS)
    guardian =models.CharField(max_length=60)
    guardian_number= models.IntegerField(max_length=10)
    guardian_relationship= models.CharField(null=True ,max_length=10)
    guardian_region=models.CharField(max_length=10)
    emergency_contact=models.IntegerField(max_length=10)
    
    def __str__(self):
        return f'{self.user.email} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class Students(models.Model):
    name=models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    age=models.IntegerField(null=True)
    course = models.TextField()
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.course