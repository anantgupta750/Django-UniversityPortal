from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import DateField
# from django.db.models.expressions import F
# from django.db.models.fields import DateField
from django.utils import timezone

# from universityportal.university.views import feedback

# Create your models here.
class Notice(models.Model):
    notice_id= models.AutoField(primary_key=True)
    notice_text= models.CharField(max_length=100,null=False)
    date= models.DateField(null=False)
    def __str__(self):
        return self.notice_text
class Contact(models.Model):
    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=50,null=False)
    phone=models.CharField(max_length=10,null=False)
    your_query=models.TextField()
    date=models.DateField(default=timezone.now) 
    def __str__(self):
        return self.name
class Feedback(models.Model):
    name=models.CharField(max_length=45,null=False)
    email=models.CharField(max_length=45,null=False)
    rating=models.IntegerField()
    feedback=models.TextField()
    date=models.DateField(default=timezone.now)
    def __str__(self) :
        return self.name

class Course(models.Model):
    courseid=models.CharField(max_length=30,primary_key=True,null=False)
    course_name=models.CharField(max_length=30,null=False)
    def __str__(self):
        return self.course_name
class Student(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id=models.CharField(max_length=40,null=False,primary_key=True)
    student_name=models.CharField(max_length=40,null=False)
    student_email=models.EmailField(max_length=50,null=False)
    student_pass=models.CharField(max_length=50,null=False,default="")
    student_phone=models.CharField(max_length=10,null=False)
    date=models.DateField(default=timezone.now) 
    student_pic=models.ImageField(max_length=100,upload_to="university/studentpic",default="")
    def __str__(self):
        return self.student_name

# class Registration(models.Model):
#     email=models.CharField(null=False,max_length=50)
#     password=models.CharField(null=False,max_length=20)
#     fname=models.CharField(null=False,max_length=20)
#     lname=models.CharField(null=False,max_length=20)
#     def __str__(self):
#         return self.fname

class Department(models.Model):
    dept_id=models.CharField(max_length=45, primary_key=True)
    dept_name=models.CharField(max_length=100,null=False)
    hod_name=models.CharField(max_length=50,null=False)
    hod_pic=models.ImageField(max_length=100,upload_to="university/studentpic",default="")
    def __str__(self):
        return self.dept_id

class Events(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=50,null=False)
    event_venue=models.CharField(max_length=100,null=False)
    event_description=models.CharField(max_length=100,null=False,default="")
    event_pic=models.ImageField(max_length=100,upload_to="university/studentpic",default="")
    event_date=models.DateField(default=timezone.now)
    event_organiser=models.CharField(max_length=100,null=False,default="")
    def __str__(self):
        return self.event_name