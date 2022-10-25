from .models import Post
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views import View
from django.urls import reverse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
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

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "ingridients": post.ingridients.all(),
            "comment_input_section": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/single-post-recipe.html", context)

    def post(self, request, slug):
        comment_input_section = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_input_section.is_valid():
            comment = comment_input_section.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("single-recipe-page", args=[slug]))

        context = {
            "post": post,
            "ingridients": post.ingridients.all(),
            "comment_input_section": comment_input_section,
            "comments": post.comments.all().order_by("-id")
        }

        return render(request, "blog/single-post-recipe.html", context)


# class SingleRecipeView(DetailView):
#     template_name = "blog/single-post-recipe.html"
#     model = Post

#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         data["ingridients"] = self.object.ingridients.all()
#         data["comment_input_section"] = CommentForm()
#         return data
