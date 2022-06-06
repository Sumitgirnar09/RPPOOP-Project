from curses.ascii import HT
from email import message
import email
from http.client import HTTPResponse
from tkinter.messagebox import QUESTION
from turtle import goto
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Student
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from exam.models import Result,Question
from student.models import Student
from exam import models as QMODEL


# std=Result.objects.all()
# ques=Question.objects.all()
# Create your views here.

Question=Question.objects.all()
Student=Student.objects.all()
Result=Result.objects.all()

def home(request):
    return render(request,'student/home.html')

def register(request):
    print("Entered in views register function")
    if request.method=="POST":
        print("request is sent", request)
        f_name=request.POST.get('f_name', '')
        l_name=request.POST.get('l_name', '')
        username=f_name+"@"+"coep"
        branch=request.POST.get('branch')
        email=request.POST.get('email', '')
        mis=request.POST.get('mis','')
        pass1=request.POST.get('pass1','')
        pass2=request.POST.get('pass2','')
        
       
        # if (pass1!= pass2):
        #      messages.error(request, " Passwords do not match")
        #      return redirect('home')
         
        print(f_name,l_name,branch,email)
        student = Student(f_name=f_name,l_name=l_name,branch=branch, email=email,mis=mis)
        student.save()
        
           # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= f_name
        myuser.last_name= l_name
        myuser.branch=branch
        myuser.email=email
        myuser.mis=mis
        myuser.save()
        # dict={"name":f_name}
        print("data created")
        messages.info(request, 'Your password has been changed successfully!')
        # messages.success(request, " Your  has been successfully created")
        return redirect('studenthome')

    return render(request, "student/register.html")

def handeLogin(request):
    # return render(request,"student/afterlogin.html")
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            
            login(request, user)
            # dict={name:user.name}
            messages.success(request, "Successfully Logged In")
         
            return render(request,"student/afterlogin.html")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return redirect("home")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("home")

def display_quiz(request):
    # global Question,Student,Result
    # Question=Question.objects.all()
    # Student=Student.objects.all()
    # Result=Result.objects.all()
    details={"question":Question,"student":Student,"result":Result}
    # print("request.user in quiz.html",user)
    print("user in quiz.html",request.user)
    return render(request,"student/quiz.html",details)

def test(request):
    return render(request,"student/test.html")

# @property
def result(request):
    Marks=0
    Correct=0
    Wrong=0
    # Question_details=Question.
    if request.user.is_authenticated:
        print("User is login",request.user.email)
        # Searching Student object corresponding to user
        active_student="student"
        for student in Student:
            if student.email==request.user.email:
                active_student=student
        print('active_student',active_student)
        # print(active_student.mis)
                
    #     print("User is ",request.user.email)
    # else:
    #     print("not logged in")
        if request.method=="POST":
            for q in Question:
                print("Actual Answer",q.answer)
                print("Written Answer",request.POST.get(q.question))
                if(q.answer)==request.POST.get(q.question):
                    Correct+=1
                    Marks=Marks+5
                else:
                    Wrong+=1
            mark_details={"marks":Marks,"Correct":Correct,"Wrong":Wrong}
            print("marks",Marks)
            print("Correct ",Correct)
         # updating details to result model
    #   student = models.ForeignKey(Student,on_delete=models.CASCADE)
    # Correct_ques=models.PositiveIntegerField()
    # Wrong_Ques=models.PositiveIntegerField()
    # marks = models.PositiveIntegerField()
    # date = models.DateTimeField(auto_now=True)
    
            result = QMODEL.Result()
            result.student=active_student
            result.marks=Marks
            result.Correct_ques=Correct
            result.Wrong_Ques=Wrong
            result.save()
            print("Model Saved Successfully")
    
    # a = Result(student = active_student,  Correct_ques = Correct,Wrong_Ques=Wrong,marks=Marks)
    # a.save()
    
    return(HttpResponse("Works Properly"))
        
        
        
        
    