from rest_framework import serializers
from .models import Movie, Genre


class Genreserializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'director', 'imdb_score', 'popularity', 'genre')
