from curses.ascii import HT
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
    return render(request,'teacher/home.html')
def login(request):
    return HTTPResponse("this is login page")
def signup(request):
    return HTTPResponse("this is signup page")
