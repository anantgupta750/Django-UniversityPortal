from django.shortcuts import redirect, render,HttpResponse
from .models import Feedback, Student, Course
from django.contrib import messages
from django.contrib.auth.models import User #import user
from django.contrib.auth import authenticate, login, logout #import login and logout and authenticate


############## student login
def student_login(request):
    if request.method=="GET":
        return render(request,'university/student_login.html')

    if request.method=="POST":
        uname=request.POST["txtusername"]
        upass=request.POST["txtpass"]
        student_obj=Student.objects.filter(student_id=uname, student_pass=upass)
        if len(student_obj)>0:
            request.session["session_id"]=uname
            context={
                "sdata": student_obj
            }
            return render(request,'university/student/student_home.html',context)
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("student_login")

############## student logout predefined
# def student_logout(request):
#     logout(request)
#     messages.success(request, "Successfully log out")
#     return redirect("student_login")

############# student logout by defining the method
def student_logout(request):
    del request.session["session_id"]
    messages.success(request,"successfully logout")
    return redirect("student_login")

############## student edit profile
def student_editprofile(request):
    s_id=request.session["session_id"]
    if request.method=="GET":
        student_obj=Student.objects.get(student_id=s_id)
        context={"data": student_obj}
        return render(request,'university/student/student_editprofile.html',context)
    if request.method=="POST":
        semail=request.POST["txtemail"]
        sname=request.POST["txtname"]
        sphone=request.POST["txtphone"]
        print(semail,sname,sphone)
        student_obj=Student.objects.filter(student_id=s_id)
        student_obj.update(student_email=semail,student_name=sname,student_phone=sphone)
        return redirect("student_home")

############### student home page
def student_home(request):
    s_id=request.session["session_id"]
    student_obj=Student.objects.filter(student_id=s_id)
    context={"sdata": student_obj}
    return render(request,'university/student/student_home.html',context)
############## Student course page
def student_course(request):
    courseobjset=Course.objects.all()
    context={
        "courseinfo":courseobjset
    }
    return render(request,'university/student/student_course.html',context)


########### student feedback page
def student_feedback(request):
    s_id=request.session["session_id"]
    if request.method=="POST":
        s_obj=Student.objects.get(student_id=s_id)
        sname=s_obj.student_name
        semail=s_obj.student_email
        srate=request.POST["rate"]
        sfeed=request.POST["txtfeed"]
        feedback=Feedback(name=sname,email=semail,rating=srate,feedback=sfeed)
        feedback.save()
        messages.success(request,"Thankyou for your feedback")
        return redirect("student_home")

    return render(request,'university/student/student_feedback.html')