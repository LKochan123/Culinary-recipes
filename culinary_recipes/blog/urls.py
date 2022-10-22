from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name='starting-page'),
    path("baza-przepisow", views.all_recipes, name='all-recipes-page'),
    path("baza-przepisow/<slug:slug>", views.single_recipe, name='single-recipe-page')
]
