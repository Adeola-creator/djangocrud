from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Post


class PostListView(ListView):
    model= Post


class PosCreateView(CreateView):
    model= Post
    fields= "__all__"
    success_url= reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model= Post

class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

