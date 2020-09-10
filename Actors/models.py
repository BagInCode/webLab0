from django.db import models


class Film(models.Model):
    Name = models.CharField('FilmName', max_length=100)
    Year = models.IntegerField('YearOfCreation')
    Poster = models.ImageField(upload_to='Films')

    def __str__(self):
        return self.Name


class Actor(models.Model):
    Name = models.CharField('ActorName', max_length=100)
    Year = models.IntegerField('YearOfBirth')

    def __str__(self):
        return self.Name


class FilmActor(models.Model):
    FilmId = models.ForeignKey(Film, on_delete=models.CASCADE)
    ActorId = models.ForeignKey(Actor, on_delete=models.CASCADE)