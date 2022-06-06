from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('studentclick', views.studentclick_view),
    path('',views.home,name='teacherhome'),
    path('teacherlogin',views.login,name='teacherlogin'),
    path('teachersignup', views.signup,name='teachersignup'),
]
