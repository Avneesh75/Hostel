from operator import imod
from django.shortcuts import redirect, render
from .models import Student,Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def Index(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'home.html')

def Register(request):
    return render(request,'register.html')

def UserRegister(request):
    if request.method =="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        course = request.POST['course']
        gender = request.POST['g']
        dob = request.POST['dob']
        aadhar = request.FILES['adhar_no']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        #First we will validate that user already exist
        user = User.objects.filter(username=email)

        if user:
            message = "User already exist"
            return render(request,'register.html',{'msg':message})

        else:
            if password==cpassword:
                user = User.objects.create_user(username=email,password=password)
                newuser = Student.objects.create(user=user,First_Name=fname,
                                                Last_Name=lname,
                                                Contact=contact,
                                                Course=course,
                                                Gender=gender,
                                                Dob=dob,
                                                Aadhar_no=aadhar,
                                                )
                messages.error(request,"Register Successfully")
                return redirect("login")
            else:
                message = "Password and Confirm Password Doesnot Match"
                return render(request,'register.html',{'msg':message})

def Login(request):
    return render(request,'login.html')

def UserLogin(request):
    if request.method =='POST':
        email=request.POST['email']
        password=request.POST['password']

        # checking the emailid with database
        user = authenticate(username=email,password=password)

        if user:
            login(request,user)
            messages.success(request,"Login Successfully!!!")
            return redirect("visitors")

        else:
            messages.error(request,"Please check username and password")
            return redirect("login")


def Room(request):
    return render(request,'room.html')

def Visitors(request):
    return render(request,'visitors.html')

def Admindash(request):
    return render(request,'admindash.html')


def Contactus(request):
    if request.method=='POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['emailadd']
        contact = request.POST['phoneno']
        msg= request.POST['message']

        user = Contact.objects.filter(Email=email)

        if user:
            messages.error(request,"You Send the all details already")
            return render(request,'home.html')
        
        else:
            newuser = Contact.objects.create(Firstname=fname,
                                                Lastname=lname,
                                                Contact=contact,
                                                Email=email,
                                                Message=msg    
                                            )
            messages.success(request,"Request sent Successfully")
            return redirect("Home")

def logout_view(request):
    logout(request)
    return redirect("Home")

def Edit(request):
        return render(request,"edit.html")
    


# def Edit(request):
#     if request.user.is_superuser:
#         return render(request,"edit.html")
#     else:


