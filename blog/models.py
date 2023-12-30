from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# A table in the database
class Post(models.Model):
    # fields in the table
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    # foreign key (the user model already exists)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
