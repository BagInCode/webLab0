
from django.urls import path

from . import views

urlpatterns = [
    path('actors/', views.indexActor, name='indexActors'),
    path('films/', views.indexFilms, name='indexFilms'),
    path('films/details/<int:film_id>/', views.get_film_id),
    path('films/details/<int:actor_id>/', views.get_actor_id),
    path('home/', views.indexHome, name='indexHome'),
]
