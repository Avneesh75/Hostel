from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.Home,name="Home"),
    path("index/",views.Index),
    path('register/',views.Register),
    path('userregister/',views.UserRegister,name='userregister'),
    path('login/',views.Login,name="login"),
    path('userlogin/',views.UserLogin,name='userlogin'),
    path('logout/',views.logout_view,name="logout"),
    path('edit/',views.Edit,name="edit"),
    path('room/',views.Room),
    path('visitors/',views.Visitors,name="visitors"),
    path('admindash/',views.Admindash),
    path('contactus/',views.Contactus,name='contact'),
    path('studentreg/',views.StudentReg,name='studentreg')
]
