from django.contrib import admin
from django.urls import path

# from otp import exam
from . import views
# from exam import views
urlpatterns = [
    # path('studentclick', views.studentclick_view),
    path('',views.home,name='studenthome'),
    path('register',views.register,name='studentregister'),
    # path('login',views.login,name='login'),
    path('handeLogin', views.handeLogin, name="handeLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('quiz', views.display_quiz, name="quiz"),
    path('test', views.test, name="test"),
    path('result',views.result,name="result"),
    # path('logout', views.handelLogout, name="handleLogout"),
]
