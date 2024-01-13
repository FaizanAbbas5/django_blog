from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# logic is handeled here
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

# class based views
class PostListView(ListView):
    model = Post # what model to query in order to create the list
    template_name = 'blog/home.html' # by default it is: <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # by default the list view is going to call the variable object list instead of posts
    ordering = ['-date_posted'] # by default it is ordering with oldest on the top, add '-' to have the newest on top
    paginate_by = 5

class UserPostListView(ListView):
    model = Post # what model to query in order to create the list
    template_name = 'blog/user_post.html' # by default it is: <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # by default the list view is going to call the variable object list instead of posts
    paginate_by = 5

    # to modify the query set received from the list view
    def get_queryset(self):
        # if the user exists, then it will be captured in the user variable, otherwise, it's going to return 404
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # to limit the results
        return Post.objects.filter(author=user).order_by('-date_posted')
        # the original order by will also be overwritten, so we will add it directly here
    

class PostDetailView(DetailView):
    model = Post

# The login required mixin ensures that the user is logged in before creating a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # we overwrite the form_valid method which will allow us to add an author before submitting
    def form_valid(self, form):
        form.instance.author = self.request.user
        # validate the form
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # we overwrite the form_valid method which will allow us to add an author before submitting
    def form_valid(self, form):
        form.instance.author = self.request.user
        # validate the form
        return super().form_valid(form)
    # to check if the user passes a test. We want only the original author of the post to be able to update it 
    def test_func(self):
        # .get_object() gives the exact post we are updating
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})