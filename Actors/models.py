from django.db import models


class Film(models.Model):
    Name = models.CharField('FilmName', max_length=100)
    Year = models.IntegerField('YearOfCreation')


class Actor(models.Model):
    Name = models.CharField('ActorName', max_length=100)
    Year = models.IntegerField('YearOfBirth')


class FilmActor(models.Model):
    FilmId = models.ForeignKey(Film, on_delete=models.CASCADE)
    ActorId = models.ForeignKey(Actor, on_delete=models.CASCADE)
