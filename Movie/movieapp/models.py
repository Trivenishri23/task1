from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=500)
    director = models.CharField(max_length=300)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    genre = models.ManyToManyField(Genre)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name
