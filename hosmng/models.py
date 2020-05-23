from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from multiselectfield import MultiSelectField
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save

register_as = (('Patient','Patient'),
               ('Doctor','Doctor'),)

gender = (('Male','Male'),
               ('Female','Female'),
               ('Other','Other'),)

Department = (('Emergency','Emergency'),
            ('Neurology','Neurology'),
            ('Oncology','Oncology'),
            ('Cardiology','Cardiology'),
            ('OPD','OPD'),
            ('Dental','Dental'),)

status = (('Completed','Completed'),
('Pending','Pending'),)

stat = (('Active','Active'),
('Inactive','Inactive'))

blood_gr = (
    ('A+', 'A+ Type'),
    ('B+', 'B+ Type'),
    ('AB+', 'AB+ Type'),
    ('O+', 'O+ Type'),
    ('A-', 'A- Type'),
    ('B-', 'B- Type'),
    ('AB-', 'AB- Type'),
    ('O-', 'O- Type'),
)
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    user = models.OneToOneField( User, null=True,blank=True, on_delete = models.CASCADE)
    phone = models.CharField(null=True,blank=True,max_length=20)
    email = models.EmailField(null=True,blank=True)
    Gender = MultiSelectField(choices=gender)
    Age = models.IntegerField(null=True)
    address =  models.CharField(max_length=200,null=True)
    date = models.DateField(auto_now_add=True,null=True,blank=True)
    outstanding = models.IntegerField(null=True,blank=True)
    paid = models.IntegerField(null=True,blank=True)
    blood_group = models.CharField(null=True,blank=True,choices=blood_gr,max_length=20)
    med_reps = models.FileField(upload_to='files',null=True,blank=True)
    case_paper = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    user = models.OneToOneField( User, null=True,blank=True, on_delete = models.CASCADE)
    phone = models.CharField(null=True,blank=True,max_length=20)
    email = models.EmailField(null=True,blank=True)
    Gender = MultiSelectField(choices=gender)
    Age = models.IntegerField(null=True)
    address =  models.CharField(max_length=200,null=True)
    date_avail = models.DateField(null=True,blank=True)
    time_avail = models.TimeField(null=True,blank=True)
    department = models.CharField(max_length=30,null=True,blank=True,choices=Department)
    attendance = models.CharField(max_length=30,null=True,blank=True)
    salary = models.CharField(max_length=30,null=True,blank=True)
    status = models.CharField(null=True,blank=True,choices=stat,max_length=20)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    doc_name = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE,related_name='doctor1')
    pat_name = models.ForeignKey(User,null=True,blank=True, on_delete = models.CASCADE,related_name='patient1')
    status = models.CharField(null=True,blank=True,choices=status,max_length=20)

class Medical(models.Model):
    prescription = models.CharField(max_length=300,null=True,blank=True)
    disease = models.CharField(max_length=300,null=True,blank=True)
    invoice = models.ImageField(upload_to='images',default="Not present")
    payment = models.CharField(max_length=300,null=True,blank=True)
    docname = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE,related_name="doctorto")
    patname = models.ForeignKey(User,null=True,blank=True, on_delete = models.CASCADE,related_name="patientto")
    date = models.DateField(null=True,blank=True)
    Outstanding = models.IntegerField(null=True,blank=True)
    total_amt = models.IntegerField(null=True,blank=True)



    def __int__(self):
        return self.date

class group(models.Model):
    group = models.CharField(max_length=20,null=True,blank=True,choices=register_as)
