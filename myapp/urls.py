from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.Home,name="Home"),
    path("index/",views.Index),
    path('register/',views.Register,name="register"),
    path('userregister/',views.UserRegister,name='userregister'),
    path('login/',views.Login,name="login"),
    path('userlogin/',views.UserLogin,name='userlogin'),
    path('logout/',views.logout_view,name="logout"),
    path('edit/',views.Edit,name="edit"),
    path('notification/',views.notification,name="notification"),
    path('adminnoti/',views.Adminnoti,name="adminnoti"),
    path('addnotification/',views.Addnotification,name="addnotification"),
    path('roombook/',views.room,name="roombook"),
    path('roomlist/',views.roollist,name='roomlist'),
    path('visitors/',views.Visitors,name='visitors'),
    path('studentlist/',views.studentList,name="studentlist"),
    path('contactus/',views.Contactus,name='contact'),
    path('view-student/',views.view_student,name='view_student'),
    path('studentreg/',views.StudentReg,name='studentreg'),
    path('studentlog/',views.Studentlog,name='studentlog'),
    path('adminreg/',views.AdminReg,name='adminreg'),
    path('adminlog/',views.AdminLog,name='adminlog'),
    path('adminhome/',views.AdminHome,name='adminhome'),
    path('adminedit/<int:id>',views.Adminedit,name='adminedit'),
    path('mess/',views.mess,name='mess'),
    path('messedit/<int:id>',views.messedit,name='messedit'),
    path('messhome/',views.Messhome,name='messhome'),
    path('room/',views.view_room,name='view_room'),
    path('add-room/',views.add_room,name='add_room'),
    path('edit-room/<int:id>/',views.edit_room,name='edit_room'),
    path('delete-room/<int:id>/',views.delete_room,name='delete_room'),
]
