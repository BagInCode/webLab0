from django.conf.urls.static import static
from django.urls import path

from webLab0 import settings
from . import views

urlpatterns = [
    path('actors/', views.indexActor, name='indexActors'),
    path('films/', views.indexFilms, name='indexFilms'),
    path('films/details/<int:film_id>/', views.get_film_id),
    path('actors/details/<int:actor_id>/', views.get_actor_id),
    path('', views.indexHome, name='indexHome'),
]