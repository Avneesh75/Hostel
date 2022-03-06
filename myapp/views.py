from django.shortcuts import redirect, render,HttpResponse
from .models import Booking, Student,Contact,AdminStudent,Room
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View
# Create your views here.
def Index(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'home.html')

def Register(request):
    if not request.user.is_authenticated:

        return render(request,'register.html')
    else:
        return redirect("Home")

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
            return redirect("Home")

        else:
            messages.error(request,"Please check username and password")
            return redirect("login")


def room(request):
    if request.method=='POST':
        student=request.POST['student']
        room=request.POST['room']
        amount=request.POST['amount']
        user = User.objects.get(id=student)
        room = Room.objects.get(id=room)
        newuser = Booking.objects.create(user=user,statu = "allow",room=room,amount=amount)
        return redirect("Home")
    room = Room.objects.all()
    use = Student.objects.all()
    book = Booking.objects.all()
    for i in book:
        room= room.exclude(id=i.room.id)
    return render(request,'room.html',{'room':room,'user':use})

def Visitors(request):
    return render(request,'visitors.html')

def Admindash(request):
    stu_data = Student.objects.all()
    return render(request,'table.html',{'studata':stu_data})

def Adminedit(request,id):
    data = Student.objects.filter(id=id)
    return render(request,'adminedit.html',{'key2':data})

def view_student(request):
    data = Student.objects.all()
    return render(request,'adminedit.html',{'key2':data})



# def get(request):
#     stu_data = Student.objects.all()
#     return render(request,'table.html',{'studata':stu_data})



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
    #fetching the data for particular id
    get_data = Student.objects.filter(user=request.user.id)
    user = User.objects.get(id=request.user.id)
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        course = request.POST['course']
        dob = request.POST['dob']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            Student.objects.filter(user=request.user.id).update(First_Name=fname,Last_Name=lname,Dob=dob,Contact=contact,Course=course)
            user.set_password(password)
            user.save()
            user=authenticate(username=user.username,password=password)
            if user:

                login(request,user)
            return redirect("Home")
        else:
            message = "Password and Confirm Password Doesnot Match"
            return render(request,'edit.html',{'msg':message})   
    return render(request,"edit.html",{"key1":get_data})

def EditDetails(request):
    pass



# <----------------Admin Side work----------------------------->

def StudentReg(request):
    if request.user.is_superuser:
        return render(request,"adminreg.html")
    else:
        pass

def Studentlog(request):
    if request.user.is_superuser:
        return render(request,"adminlogin.html")
    else:
        pass

def AdminReg(request):
    if request.method =="POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['your_email']
        contact = request.POST['contact']
        course = request.POST['course']
        gender = request.POST['g']
        dob = request.POST['dob']
        aadharimg = request.FILES['aadhrimg']
        profileimg = request.FILES['proimg']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']

        user = User.objects.filter(username=email)

        if user:
            message = "User already exist"
            return render(request,'adminreg.html',{'msg':message})

        else:
            if password==cpassword:
                user = User.objects.create_user(username=email,password=password)
                newuser = AdminStudent.objects.create(user=user,First_Name=fname,
                                                Last_Name=lname,
                                                Contact=contact,
                                                Course=course,
                                                Gender=gender,
                                                Dob=dob,
                                                Aadhar_pic=aadharimg,
                                                Profile_pic=profileimg
                                                )
                messages.error(request,"Register Successfully")
                return redirect("login")
            else:
                message = "Password and Confirm Password Doesnot Match"
                return render(request,'admin.html',{'msg':message})


def AdminLog(request):
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


