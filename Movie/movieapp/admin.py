from django.contrib import admin
from .models import Movie, Genre


# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    pass

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'imdb_score', 'director', 'popularity']
    list_filter =['genre']
    search_fields = ['name', 'director']
    pass

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)

'''
admin-Triveni
pass- movie123
'''