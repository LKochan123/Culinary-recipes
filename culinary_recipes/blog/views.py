from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views import View
from django.urls import reverse
from django.shortcuts import render
from .models import Post
from .forms import CommentForm


# Create your views here.


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "starting_page_posts"

    def get_queryset(self):
        N = 3
        latest_N_posts = super().get_queryset()[:N]
        return latest_N_posts


class AllRecipesView(ListView):
    template_name = "blog/all-recipes.html"
    model = Post
    context_object_name = "all_recipes"
    ordering = ["-rating"]


class SingleRecipeView(View):

    def is_fav_button(self, request, post_id):
        stored_recipes = request.session.get("stored_recipes")

        if stored_recipes is None:
            is_fav = False
        else:
            is_fav = post_id in stored_recipes

        return is_fav

    def help_context_method(self, request, comment_input, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "ingridients": post.ingridients.all(),
            "comment_input_section": comment_input,
            "comments": post.comments.all().order_by("-id"),
            "is_fav": self.is_fav_button(request, post.id)
        }

        return context

    def get(self, request, slug):
        comment = CommentForm()
        context = self.help_context_method(request, comment, slug)

        return render(request, "blog/single-post-recipe.html", context)

    def post(self, request, slug):
        comment_input_section = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_input_section.is_valid():
            comment = comment_input_section.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("single-recipe-page", args=[slug]))

        context = self.help_context_method(
            request, comment_input_section, slug)

        return render(request, "blog/single-post-recipe.html", context)


class FavouriteView(View):
    def get(self, request):
        stored_recipes = request.session.get("stored_recipes")

        context = {}

        if stored_recipes is None or not len(stored_recipes):
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_recipes)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/favourites-recipes.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_recipes")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_recipes"] = stored_posts

        return HttpResponseRedirect("/")
