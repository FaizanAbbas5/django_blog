from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name= 'blog-home'), #it has to be converted into an actual view
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #to add a variable use <>, we use the ID of the post (primary key) as part of the route
                                #we can also specify what kind of variable it is. pk is a convention (it can be changed though in the view)
    path('post/new/', PostCreateView.as_view(), name= 'post-create'), # template should be <model>_form
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name= 'post-update'), # same template as create view
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), #post_confirm_delete.html
    path('about/', views.about, name= 'blog-about')
]