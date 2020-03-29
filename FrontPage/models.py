from django.db import models

# Create your models here.
class User(models.Model):
    FullName=models.CharField(max_length=120)
    Mail=models.CharField(max_length=120)
    Location=models.CharField(max_length=140)
    Password=models.CharField(max_length=140)

class User_Activity(models.Model):
    FullName=models.CharField(max_length=120)
    location=models.CharField(max_length=140)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
