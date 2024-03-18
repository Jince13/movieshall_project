from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    username = models.CharField(primary_key=True,max_length=30)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_img = models.ImageField(upload_to='pics/user_img')
    password = models.CharField(max_length=35)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.username


# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField(null=True, blank=True)
#     image = models.ImageField(upload_to='user_images/', null=True, blank=True)
#
#     def __str__(self):
#         return self.username


