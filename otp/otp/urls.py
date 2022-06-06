from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    # Go to url of teacher
    path('teacher/',include('teacher.urls')),
    # Go to url of student
    path('student/',include('student.urls')),
    
]
