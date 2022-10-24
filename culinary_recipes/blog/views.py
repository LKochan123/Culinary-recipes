from .models import Post
from django.views.generic import ListView, DetailView
from django.views import View
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


class SingleRecipeView(DetailView):
    template_name = "blog/single-post-recipe.html"
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["ingridients"] = self.object.ingridients.all()
        data["comment_input_section"] = CommentForm()
        return data
