from django import views
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(" ",views.Index),
    path('home/',views.Home),
    path('register/',views.Register),
    path('login/',views.Login),
    path('room/',views.Room),
    path('visitors/',views.Visitors),
    path('admindash/',views.Admindash),

]
