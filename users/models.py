from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    # One to one relation with the existing user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # If we don't have this, whenever we print out a profile, it will say Profile Object
    # so we want to be more specific/ descripive, we tell it how we want to print it out
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        # save method of the parent class
        super().save()
        # To open the image of the current profile instance
        img = Image.open(self.image.path)

        # resizing image to 300 pixels
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            # save it back to the same path to override the large image
            img.save(self.image.path)