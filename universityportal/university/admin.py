from django.contrib import admin

#from universityportal.university.views import feedback

# Register your models here.
from .models import Course, Notice,Contact,Feedback, Student,Department,Events
admin.site.register(Notice)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Course)
admin.site.register(Student)
# admin.site.register(Registration)
admin.site.register(Department)
# admin.site.register(Events)