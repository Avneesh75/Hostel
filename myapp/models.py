from email.message import Message
from tkinter.messagebox import YES
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

gender =(("male", "male"),
    ("female", "female"),

)
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    First_Name = models.CharField(max_length=50,null=False)
    Last_Name = models.CharField(max_length=50,null=False)
    Dob = models.DateField(auto_now=False,null=True)
    Contact = models.CharField(max_length=15,null=False)
    Aadhar_no = models.ImageField(upload_to="img/")
    Course = models.CharField(max_length=20)
    Gender = models.CharField(choices=gender,max_length=15)

    def __str__(self):
        return self.First_Name

class Room(models.Model):
    Details = models.CharField(max_length=150)
    Room_no = models.CharField(max_length=5,null=True)
    Beds = models.CharField(max_length=5)
    Rent = models.CharField(max_length=5)
    Floor = models.CharField(max_length=5)
    Image = models.ImageField(upload_to='room_img',null=True)

    def __str__(self):
        return self.Room_no

class Contact(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    Contact = models.CharField(max_length=15)
    Email = models.EmailField(max_length=50)
    Message = models.CharField(max_length=200)

    def __str__(self):
        return self.Email,self.Firstname

status = (
    ('pending' ,'pending'),
    ('allow' ,'allow'),
    ('disallow' ,'disallow')
    )
class Booking(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    room = models.ForeignKey(Room,models.CASCADE)
    amount = models.CharField(max_length=10,null=True)
    statu = models.CharField(max_length=10,choices=status, null=True)
    booking_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room

class AdminStudent(models.Model):
    
    First_Name = models.CharField(max_length=50,null=False)
    Last_Name = models.CharField(max_length=50,null=False)
    Dob = models.DateField(auto_now=False,null=True)
    Contact = models.CharField(max_length=15,null=False)
    Aadhar_pic = models.ImageField(upload_to="img/")
    Profile_pic = models.ImageField(upload_to="img/")
    Course = models.CharField(max_length=20)
    #Gender = models.CharField(choices=gender,max_length=15)

    def __str__(self):
        return self.First_Name

class Mess(models.Model):
    day=models.CharField(max_length=20)
    item=models.CharField(max_length=20)
    price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.day

class Notification(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=150)
    status=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

