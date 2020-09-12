from django.db import models


class Film(models.Model):
    filmName = models.CharField('FilmName', max_length=200)
    filmYear = models.IntegerField('YearOfCreation')
    filmPoster = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name='Изображение')

    def __str__(self):
        return self.filmName

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Actor(models.Model):
    actorName = models.CharField('ActorName', max_length=200, default='default_name')
    actorYear = models.IntegerField('YearOfBirth')

    def __str__(self):
        return self.actorName

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class FilmActor(models.Model):
    FilmId = models.ForeignKey(Film, on_delete=models.CASCADE)
    ActorId = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
