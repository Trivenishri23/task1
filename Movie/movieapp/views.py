from django.shortcuts import render

from rest_framework import  generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import  Movieserializer


# Create your views here.
class Indexview(APIView):
    allowed_metothd = ['GET']
    serializer_class = Movieserializer

    def get(self, request, *args, **kwargs):
        query = Movie.objects.all()

        name = request.query_params.get('name', None)
        if name is not None:
            query = query.filter(name__icontain=name)

        director = request.query_params.get('director', None)
        if director is not None:
            query = query.filter(director__icontain=director)

        genre = request.query_params.get('genre', None)
        if genre is not None:
            query = query.filter(genre__name__icontain=genre)

        director = request.query_params.get('director', None)
        if director is not None:
            query = query.filter(director__icontain=director)

        serializer = self.serializer_class(query, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)