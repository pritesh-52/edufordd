from django.db import models
from django.forms import ModelForm,Textarea


class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=40)
class Commet(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    message=models.CharField(max_length=40)

# Create your models here.
