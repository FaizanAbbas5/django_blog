from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    # One to one relation with the existing user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # If we don't have this, whenever we print out a profile, it will say Profile Object
    # so we want to be more specific/ descripive, we tell it how we want to print it out
    def __str__(self):
        return f'{self.user.username} Profile'