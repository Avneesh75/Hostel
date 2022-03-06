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
    path('room/',views.room,name="roomallocate"),
    path('visitors/',views.Visitors,name="visitors"),
    path('admindash/',views.Admindash),
    path('contactus/',views.Contactus,name='contact'),
    path('view-student/',views.view_student,name='view_student'),
    path('studentreg/',views.StudentReg,name='studentreg'),
    path('studentlog/',views.Studentlog,name='studentlog'),
    path('adminreg/',views.AdminReg,name='adminreg'),
    path('adminlog/',views.AdminLog,name='adminlog'),
    path('adminedit/<int:id>',views.Adminedit,name='adminedit'),
]
