from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def starting_page(request):

    N = 3
    the_latest_N_recipes = Post.objects.all().order_by("-date")[:N]

    return render(request, "blog/index.html", {
        "posts": the_latest_N_recipes
    })


def all_recipes(request):
    return render(request, "blog/all-recipes.html", {
        "all_posts": Post.objects.all().order_by("date")
    })


def single_recipe(request, slug):
    id_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/single-post-recipe.html", {
        "post": id_post,
        "ingridients": id_post.ingridients.all()
    })
