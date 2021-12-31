from django.http.response import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from django.views.generic.base import View
from .models import Contact, Course,Notice,Student,Department
from django.contrib import messages
from django.contrib.auth.models import User #import user
from django.contrib.auth import authenticate, login, logout #import login and logout and authenticate
from django.views import View
from django.http import JsonResponse

# Create your views here.

def registration(request):
    if request.method=="POST":
        print(request.POST)
        remail=request.POST["txtemail"]
        ruser=request.POST["txtusername"]
        rpass=request.POST["txtpass"]
        rfname=request.POST["txtname"]
        rlname=request.POST["txtname1"]

        if len(rpass)<8 or not ruser.isalnum():
            messages.error(request,"Password must be greater than 8 and is not alpha numeric")
            return redirect("registration")
        print(remail,ruser,rpass,rfname,rlname)
        userobj= User.objects.create_user(ruser, remail, rpass)
        userobj.first_name= rfname
        userobj.last_name= rlname
        userobj.save()
        messages.success(request, "Thankyou for registration")
    return render(request,'university/registration.html')

def contact(request):
    # return HttpResponse("<h3> This is 7505454380 my contact no</h3>")
    if request.method=="POST":
        print(request.POST)#dictionary....will accept user input in the form of dictionary
        cname=request.POST["txtname"]
        cemail=request.POST["txtemail"]
        cphone=request.POST["txtphonenumber"]
        cquery=request.POST["txtquery"]
        # print(cname,cemail,cphone,cquery)
        contact_obj=Contact(name=cname,email=cemail,phone=cphone,your_query=cquery)
        contact_obj.save()
        print("contact added successfully")
        messages.success(request, "Thankyou for contacting us")
        


    return render(request,'university/contact.html')
def feedback(request):
    # return HttpResponse("<h1>This is the feeback page</h1>")
    if request.method=="POST":
        print(request.POST)
    return render(request,'university/feedback.html')
def index(request):
    return render(request,'university/index.html')
# important--> to view on homepage (content)
def homepage(request):
    noticeobjset=Notice.objects.all() #show all objects in queryset
    hodobjset1=Department.objects.all()[:1]
    hodobjset2=Department.objects.all()[1:2]
    #print(noticeobjset)
    context={
        "noticeKey":noticeobjset,  #binding object in dictionary
        "hodinfo1":hodobjset1,
        "hodinfo2":hodobjset2,
    }
    return render(request,'university/homepage.html',context)

    # return render(request,'university/homepage.html',notice_dict)

def aboutpage(request):
    context={"abt":"ABOUT AKTU","address":",LUCKNOW"}
    return render(request,'university/aboutpage.html',context)
def course(request):
    courseobjset=Course.objects.all()
    context={
        "courseinfo":courseobjset
    }
    return render(request,'university/course.html',context)

def viewstudents(request):
    studentsobjset=Student.objects.all()
    context={"studentinfo":studentsobjset}
    return render(request,'university/viewstudents.html',context)

########## Login class     this is same as the the user login but with the help of the class 

class Login(View):          #login is the sub class of the view class
    def get(self,request):
        return render(request, 'university/user_login.html')
    def post(self,request):
        uname=request.POST["txtusername"]
        upass=request.POST["txtpass"]
        custom_user=authenticate(request,username=uname,password=upass)
        if custom_user is not None:
            login(request,custom_user)
            return render(request,"university/user/loginpage.html")
        else:
            messages.error(request,"Username or password not matched.")
            return redirect("user_login")

# def user_login(request):
#     if request.method=="POST":
#         uname=request.POST["txtusername"]
#         upass=request.POST["txtpass"]
#         custom_user=authenticate(request,username=uname,password=upass)
#         if custom_user is not None:
#             login(request,custom_user)
#             return render(request,"university/user/loginpage.html")
#         else:
#             messages.error(request,"Username or password not matched.")
#             return redirect("user_login")
#     return render(request,'university/user_login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Successfully log out")
    return redirect("user_login")

def edit_profile(request):
    if request.method=="GET":
        return render(request,"university/user/edit_profile.html")
    if request.method=="POST":
        email=request.POST["txtemail"]
        fname=request.POST["txtfname"]
        lname=request.POST["txtlname"]
        request.user.email=email
        request.user.first_name=fname
        request.user.last_name=lname
        request.user.save()
        return redirect("loginpage")
    return render(request,"university/user/edit_profile.html")

def loginpage(request):
    return render(request,"university/user/loginpage.html")

def validate_username(request):
    print("function calling")
    username=request.GET.get('txtusename',None)
    print(username)
    myuserqueryset=User.objects.filter(username=username)
    print(myuserqueryset)
    for u in myuserqueryset:
        print("hello",u.username)
    data={'is_taken':"noteexits"}
    if myuserqueryset.exists():
        data={'is_taken':"exits"}
        return JsonResponse(data)
    else:
        return JsonResponse(data)