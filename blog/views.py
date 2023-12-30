from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# data to be passed in the template

def home(request):
    # we put our data into a dictionary
    # the key here is what is going to be accessible in our templates
    context = {
        'posts': Post.objects.all()
    }
    # we pass context as the third argument
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})