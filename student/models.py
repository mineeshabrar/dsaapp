from django.db import models
from .models import *
# Create your models here.

class student(models.Model):
    sid = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #branch = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    def __str__(self):
        return self.first_name
    
class societies(models.Model):
    student_details = models.ForeignKey(student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    proficiency = models.BooleanField()   ## add the function for unique proficiency
    def __str__(self):
        return self.name
    
class events(models.Model):
     student_details = models.ForeignKey(societies, on_delete=models.CASCADE)
     event_name = models.CharField(max_length=100)   
     def __str__(self):
        return self.event_name




