from django.db.models.signals import post_save #triggerd when an object is saved
from django.contrib.auth.models import User #acts as a sender (sends the signal)
from django.dispatch import receiver #a receiver function to receive a signal and then performs some task
from .models import Profile #we will be creating a profile in our function

# Here we use a decorator that we can add to the function
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()