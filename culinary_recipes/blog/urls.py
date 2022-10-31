from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name='starting-page'),
    path("baza-przepisow", views.AllRecipesView.as_view(), name='all-recipes-page'),
    path("baza-przepisow/<slug:slug>",
         views.SingleRecipeView.as_view(), name='single-recipe-page'),
    path("ulubione", views.FavouriteView.as_view(), name="favourites"),
    path("zaloguj-sie", views.SignInView.as_view(), name="sign-in"),
    path("zarejstruj-sie", views.SignUpView.as_view(), name="sign-up")
]
