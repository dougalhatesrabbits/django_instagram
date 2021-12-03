from django.shortcuts import render
from django.views.generic import ListView, CreateView # new
from .models import Post
from django.urls import reverse_lazy # new
from .forms import PostForm # new


# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')
