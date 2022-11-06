from django.urls import path
from . import views

urlpatterns = [
    # Ogólna sekcja
    path("", views.StartingPageView.as_view(), name='starting-page'),
    path("baza-przepisow", views.AllRecipesView.as_view(), name='all-recipes-page'),
    path("baza-przepisow/<slug:slug>",
         views.SingleRecipeView.as_view(), name='single-recipe-page'),
    # Sekcja ulubionych dla zwykłych użytkowników i tych którzy posiadają konta
    path("ulubione", views.FavouriteView.as_view(), name='favourites'),
    path("ulubione/<int:id>/", views.fav_add, name='favourite-add'),
    path("ulubione-przepisy", views.favourite_list, name='favourite-list'),
    # Sekcja związana z zakładaniem konta
    path("zaloguj-sie", views.SignInView.as_view(), name='sign-in'),
    path("zarejstruj-sie", views.SignUpView.as_view(), name='sign-up'),
    path("wyloguj-sie", views.logout, name='logout')
]
