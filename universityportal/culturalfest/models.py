from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=60, null=True)
    phone=models.CharField(max_length=10)
    query=models.TextField()
    def __str__(self):
        return self.name