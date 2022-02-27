from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'home.html')

def Register(request):
    return render(request,'register.html')
 
def Login(request):
    return render(request,'login.html')

def Room(request):
    return render(request,'room.html')

def Visitors(request):
    return render(request,'visitors.html')

def Admindash(request):
    return render(request,'admindash.html')


