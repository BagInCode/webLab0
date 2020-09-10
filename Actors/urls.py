from django.urls import path

from . import views

urlpatterns = [
    path('actors/', views.indexActor, name='indexActors'),
    path('films/', views.indexFilms, name='indexFilms'),
]