from django.db import models
from .models import *
# Create your models here.

class student(models.Model):
    sid = models.IntegerField(unique=True)
    details = models.JSONField()
    def __str__(self):
        return str(self.sid)

class club(models.Model):
    club_id = models.CharField(unique=True, max_length=30)
    details = models.JSONField()
    def __str__(self):
        return self.club_id

class event(models.Model):
    event_id = models.CharField(unique=True, max_length=500)
    details = models.JSONField()
    def __str__(self):
        return self.event_id

