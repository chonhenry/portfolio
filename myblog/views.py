from django.shortcuts import render
from django.shortcuts import render, redirect
from myblog.models import Post
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from . import models
from django.urls import reverse_lazy

#def home(request):
#    return render(request, 'myblog/home.html')


class PostListView(ListView):
    context_object_name = 'posts' #default name is post_list
    model = models.Post


class PostDetailView(DetailView):
    context_object_name = 'post_detail' #default name is post
    model = models.Post
    template_name = 'myblog/post_detail.html'
    success_url = reverse_lazy("myblog:list")

class PostCreateView(CreateView):
    fields = ("author", "title", "text")
    model = models.Post
