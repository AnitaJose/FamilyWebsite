from django.db import models

# Create your models here.

class login(models.Model):
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    def __str__(self):
        return self.Username

class signup(models.Model):
    Username = models.ForeignKey(login,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    DOB = models.DateField()
    EmailID = models.EmailField()
    PhoneNumber = models.CharField(max_length=10)


    def __str__(self):
        return self.FirstName

class family(models.Model):
    FamilyHead = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    DOB = models.DateField()
    Email = models.EmailField(max_length=254)
    Photo = models.ImageField(upload_to='MEDIA_ROOT/')
    Description = models.TextField()

    def __str__(self):
        return self.Name

class Addfamilyphotos(models.Model):
    Photo = models.ImageField(upload_to='MEDIA_ROOT/')


