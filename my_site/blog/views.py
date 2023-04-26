from django.shortcuts import render, get_object_or_404
from .models import Author, Tag, Post
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .forms import CommentForm


# Create your views here.


class StartingPage(ListView):
    model = Post
    template_name = "blog/index.html"


class Posts(ListView):
    model = Post
    template_name = "blog/all-posts.html"


class PostDetail(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        context['comment_form'] = CommentForm()
        return context
