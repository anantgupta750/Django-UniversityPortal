"""universityportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from . import student_views
from .views import Login
urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('contact',views.contact,name="contact"),
    path('feedback',views.feedback,name="feedback"),
    path('index',views.index,name="index"),
    path('homepage',views.homepage,name="homepage"),
    path('aboutpage',views.aboutpage,name="aboutpage"),
    path('registration',views.registration,name="registration"),
    path('course',views.course,name="course"),
    path('viewstudents',views.viewstudents,name="viewstudents"),
    # path('user_login',views.user_login,name="user_login"),
    path('user_login',Login.as_view(),name="user_login"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('loginpage',views.loginpage,name="loginpage"),
    path('student_login',student_views.student_login,name="student_login"),
    path('student_editprofile',student_views.student_editprofile,name="student_editprofile"),
    path('student_logout',student_views.student_logout,name="student_logout"),
    path('student_home',student_views.student_home,name="student_home"),
    path('student_course',student_views.student_course,name="student_course"),
    path('student_feedback',student_views.student_feedback,name="student_feedback"),
    path('validate_username',views.validate_username, name="validate_username")

   
]
