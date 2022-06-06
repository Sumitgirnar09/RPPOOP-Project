import email
from django.db import models

# Create your models here.

# class Student(models.Model):

class Student(models.Model):
    msg_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=70, default="")
    email= models.CharField(max_length=70, default="")
    pass1= models.CharField(max_length=70, default="")
    pass2= models.CharField(max_length=70, default="")
    mis = models.CharField(max_length=50,default='')
    
    print(f_name,l_name,branch,email)
    def __str__(self):
        return self.f_name + "" + self.l_name
# print(Student.objects.all())