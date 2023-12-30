from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# data to be passed in the template
posts = [
    
    # each dictionary contains information related to a post
    {
        "author": "Faizi Baloch",
        "title": "My first post",
        "content": "Content for my first post",
        "date_posted": "25th December"
    },
    {
        "author": "Faizan",
        "title": "My Second Post",
        "content": "Content for my second post",
        "date_posted": "25 December"
    }
]

def home(request):
    # we put our data into a dictionary
    # the key here is what is going to be accessible in our templates
    context = {
        'posts': posts
    }
    # we pass context as the third argument
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})