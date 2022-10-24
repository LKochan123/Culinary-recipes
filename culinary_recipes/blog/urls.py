from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name='starting-page'),
    path("baza-przepisow", views.AllRecipesView.as_view(), name='all-recipes-page'),
    path("baza-przepisow/<slug:slug>",
         views.SingleRecipeView.as_view(), name='single-recipe-page')
]
