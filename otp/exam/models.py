from pyexpat import model
from django.db import models
from student.models import Student

class Question(models.Model):
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)
    
class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    Correct_ques=models.PositiveIntegerField()
    Wrong_Ques=models.PositiveIntegerField()
    marks = models.PositiveIntegerField()
    # date = models.DateTimeField(auto_now=True,blank=True)


    