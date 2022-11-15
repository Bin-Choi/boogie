from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render

from .serializers import MovieListSerializer, MovieSerializer, MovieNameSerializer, DirectorNameSerializer, GenreNameSerializer, ReviewSerializer
from .models import Movie, Actor, Genre, Director, Review
import requests

# Create your views here.
@api_view(['GET'])
def movie_detail(request, tmdb_id):
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

def movie_recent(request, num):
    pass

def review_recent(request, num):
    pass

# def fill_data(request):

#     url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=6f44898888940b2a302f0cdbee081d68&language=ko-KO&page=3&region=KR'
#     response = requests.get(url)
#     movie_dict = response.json()
#     movies = movie_dict['results']

#     for movie in movies:
#         m = Movie()

#         m.title = movie.get('title')
#         m.release_date = movie.get('release_date')
#         m.tmdb_id = movie.get('id')
#         m.poster_path = movie.get('poster_path')
#         m.overview = movie.get('overview')
#         # m.country = movie.get('country')
#         m.vote_average = movie.get('vote_average')
#         m.vote_count = movie.get('vote_count')
#         m.backdrop_path = movie.get('backdrop_path')
#         # m.actors = movie.get('actors')
#         # m.genres = movie.get('genres')
#         # m.director = movie.get('crews')

#         m.save()
