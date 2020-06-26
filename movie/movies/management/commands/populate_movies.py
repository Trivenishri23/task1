import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from ...models import Movie, Genre


class Command(BaseCommand):
    """
    store movies data from provided dump
    """
    def handle(self, *args, **options):
        filepath = settings.BASE_DIR + '/imdb.json'
        with open(filepath, 'r') as f:
            raw_data = f.read()
            data = json.loads(raw_data)
            k = {}
            for movie_item in data:
                k['name'] = movie_item.get('name')
                k['popularity'] = movie_item.get('99popularity')
                k['director'] = movie_item.get('director')
                k['imdb_score'] = movie_item.get('imdb_score')
                movie, created = Movie.objects.get_or_create(**k)
                genre_list = movie_item.get('genre')
                # create genre for each genre in list and attach to current movie
                for name in genre_list:
                    name = name.strip()
                    genre, created = Genre.objects.get_or_create(name=name)
                    movie.genre.add(genre)
                movie.save()
                print movie


