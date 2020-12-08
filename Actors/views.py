from django.shortcuts import render

from .models import Actor, Film


def indexActor(request):
    ActorsList = Actor.objects.order_by('-id')[:10]
    return render(request, 'Actors/list.html', {'ActorsList': ActorsList})


def indexFilms(request):
    FilmList = Film.objects.order_by('-id')[:10]
    return render(request, 'Actors/list.html', {'FilmList': FilmList})


def get_film_id(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request, "Actors/page.html", {'film': film})


def indexHome(request):
    return render(request, "Actors/home.html")


def get_actor_id(request, actor_id):
    film = Actor.objects.get(id=actor_id)
    return render(request, "Actors/ActorDetails.html", {'Actor': film})
