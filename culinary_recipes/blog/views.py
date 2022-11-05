from urllib import request
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Profile, Comment
from .forms import CommentForm
from datetime import datetime


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
    ordering = ["-date"]


class SingleRecipeView(View):

    def is_fav_button(self, request, post_id):
        stored_recipes = request.session.get("stored_recipes")

        if stored_recipes is None:
            is_fav = False
        else:
            is_fav = post_id in stored_recipes

        return is_fav

    def help_context_method(self, request, comment_input, slug):
        post = get_object_or_404(Post, slug=slug)
        is_favourite_login = False

        if post.favourites.filter(id=request.user.id).exists():
            is_favourite_login = True

        context = {
            "post": post,
            "ingridients": post.ingridients.all(),
            "comment_input_section": comment_input,
            "comments": post.comments.all().order_by("-id"),
            "is_fav": self.is_fav_button(request, post.id),
            "is_favourite_login": is_favourite_login
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
            name = request.user.username
            body = comment_input_section.cleaned_data['text']
            actual_date = datetime.now()

            c = Comment(nickname=name, date=actual_date, text=body, post=post)
            c.save()
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


class SignUpView(View):

    def get(self, request):
        return render(request, "blog/sign-up.html")

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        check_password = request.POST['check-password']

        inputs = [username, email, password, check_password]

        if self.check_inputs(inputs):
            if password == check_password:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Podany email jest już zajęty!')
                    return redirect('sign-up')
                elif User.objects.filter(username=username).exists():
                    messages.info(
                        request, 'Podana nazwa użytkownika jest już zajęta!')
                    return redirect('sign-up')
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password)
                    user.save()

                    user_model = User.objects.get(username=username)
                    new_profile = Profile.objects.create(
                        user=user_model, id_user=user_model.id)
                    new_profile.save()
                    return redirect('sign-in')
            else:
                messages.info(request, 'Hasła do siebie nie pasują!')
                return redirect('sign-up')
        else:
            messages.info(request, 'Wypełnij wszystie dane!')
            return redirect('sign-up')

    # Pomocnicza funkcja, sprawdze czy jakieś pole nie zostało puste
    def check_inputs(self, inputs):
        for input in inputs:
            if not input:
                return False
        return True


class SignInView(View):
    def get(self, request):
        return render(request, "blog/sign-in.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if (username or password):
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Błędna nazwa użytkownika lub hasło!')
                return redirect('sign-in')
        else:
            messages.info(request, 'Wypełnij powyższe pola aby się zalogować.')
            return redirect('sign-in')


@login_required
def favourite_list(request):
    new = Post.newmanager.filter(favourites=request.user)

    has_posts = True
    if new is None or len(new) == 0:
        has_posts = False

    context = {
        "posts": new,
        "has_posts": has_posts
    }

    return render(request, "blog/favourites-recipes.html", context)


@login_required
def fav_add(request, id):
    post = get_object_or_404(Post, id=id)

    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)

    return HttpResponseRedirect("/")


def logout(request):
    auth.logout(request)
    return redirect('sign-in')
