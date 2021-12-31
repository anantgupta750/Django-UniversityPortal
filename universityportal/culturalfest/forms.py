from django import forms 
from .models import Enquiry
class DemoForm(forms.Form):
    name=forms.CharField(initial="Your  Name", help_text="Honey Singh")
    email=forms.EmailField(label="Your Email", help_text="xyz@gmail.com")
    password=forms.CharField(widget=forms.HiddenInput())
    phone=forms.IntegerField(required=False,disabled=True,widget=forms.NumberInput)
    date=forms.CharField(widget=forms.DateInput)
    rollnumber=forms.IntegerField()

class Enquiryform(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields=["name","email","phone","query"]    #this will only take those value written within the list
        # fields="__all__"        #this will take all the values from the model
        


