from django.shortcuts import render

from .models import Actor, Film


def indexActor(request):
    ActorsList = Actor.objects.order_by('-id')[:10]
    return render(request, 'Actors/list.html', {'ActorsList': ActorsList})


def indexFilms(request):
    FilmList = Film.objects.order_by('-id')[:10]
    return render(request, 'Actors/list.html', {'ActorsList': FilmList})

