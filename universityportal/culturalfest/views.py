from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages


from .forms import DemoForm,Enquiryform

# Create your views here.
def home(request):
    # return HttpResponse("<h1> This is cultural fest home page</h1>")
    return render(request,'culturalfest/home.html')
########### aboutfest
def aboutfest(request):
    return render(request,'culturalfest/aboutfest.html')
##########demo form
def demoform(request):
    d=DemoForm()
    context={"myform":d}
    return render(request,'culturalfest/demoform.html',context)

#######enquiry function
def enquiry(request):
    if request.method=="POST":
        form= Enquiryform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Form has been successfully submitted")
            return redirect('home')
    if request.method=="GET":
        form=Enquiryform()
        return render(request,'culturalfest/enquiry.html',{"form":form})

