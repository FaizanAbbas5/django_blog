from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
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
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')