from django.db import models
from django.contrib.auth.models import AbstractUser
from .manage import UserManager
from rest_framework import serializers

# Create your models here.
class CustomUser(AbstractUser):
    
    username = None
    phone_number = models.CharField(max_length=120 , unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=150)
    user_profile = models.ImageField(upload_to="profile")
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
class Student(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return self.name
    
class StudentSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        

