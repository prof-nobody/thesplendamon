from django.shortcuts import render
from django.views import generic
from .models import Post
from django.shortcuts import redirect

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'


class PostDetails(generic.DetailView):
    model = Post
    template_name = 'post_details.html'


# @login_required
class PostCreation(generic.CreateView):
    model = Post
    fields = ['title', 'slug', 'author', 'content', 'status']
    template_name = 'post_create.html'

    # return redirect('home')
