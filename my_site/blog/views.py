from django.shortcuts import render, get_object_or_404
from .models import Author, Tag, Post
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views import View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


class StartingPage(ListView):
    model = Post
    template_name = "blog/index.html"


class Posts(ListView):
    model = Post
    template_name = "blog/all-posts.html"


class PostDetail(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    # should handle all get requests
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        # Todo anki

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all(),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    # should handle all post requests
    def post(self, request, slug):
        # get the submitted data from form
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        # if form data ist valid
        if comment_form.is_valid():
            # save to the database
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            # here we are redirecting the user to the url which we are getting from the urls.py
            # the slug is automatically provided by django when we run the PostDetail View in the matching url
            # so we redirecting the user to the current post
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        # if the form data is not valid we just loading the content just as in the get method

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all(),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)


# Todo anki
class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")
