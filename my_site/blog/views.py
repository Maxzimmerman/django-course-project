from django.shortcuts import render, get_object_or_404
from .models import Author, Tag, Post


# Create your views here.

def starting_page(request):
    posts_data = Post.objects.all()
    return render(request, "blog/index.html", {
        "posts": posts_data
    })


def posts(request):
    posts_all = Post.objects.all()
    return render(request, "blog/all-posts.html", {
        "all_posts": posts_all
    })


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })
