from django.db import models

# Create your models here.
class usersignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    username=models.EmailField()
    password=models.CharField(max_length=12)

class mynotes(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    myfile=models.FileField(upload_to='MyNotes')
    description=models.TextField()

class contactus(models.Model):
    created=models.DateTimeField(auto_now_add=True)    
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    message=models.TextField()


