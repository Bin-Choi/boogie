from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render

from django.contrib.auth import get_user_model

from .serializers import MovieListSerializer, MovieSerializer, MovieNameSerializer, GenreNameSerializer, ReviewSerializer
from .models import Movie, Actor, Genre, Director, Review
import requests
from django.db.models import Q

# Create your views here.
@api_view(['GET'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

def movie_recent(request, num):
    pass

def review_list_recent(request, num):
    pass

def review_list_user(request):
    pass

@api_view(['GET', 'POST'])
def review_list_movie(request, movie_pk):
    movie=Movie.objects.get(id=movie_pk)
    if request.method == 'GET':
        print('>>>>>>>>>>,>>>>>>>>>>>>>>>>>>>>>>', '1')
        other_reviews = list(Review.objects.filter(Q(movie=movie) & ~Q(user=request.user)).order_by('created_at'))
        print('>>>>>>>>>>,>>>>>>>>>>>>>>>>>>>>>>', '2')
        my_review = list(Review.objects.filter(movie=movie, user=request.user))
        # print(request.user.name, request.user.id)
        print('>>>>>>>>>>,>>>>>>>>>>>>>>>>>>>>>>', '3')
        reviews = my_review + other_reviews
        print('>>>>>>>>>>,>>>>>>>>>>>>>>>>>>>>>>', '4')
        serializer = ReviewSerializer(reviews, many=True)

        is_voted = False
        if my_review:
            is_voted = True

        data = {
            'isVoted': is_voted,
            'reviews': serializer.data,
        }
        return Response(data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user == request.user:
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_403_FORBIDDEN)

# def fill_data(request):
#     # genres
#     url_genre = f'https://api.themoviedb.org/3/genre/movie/list?api_key=6f44898888940b2a302f0cdbee081d68&language=ko-KO'
#     response = requests.get(url_genre)  # <class 'requests.models.Response'>: <Response [200]>
#     genres_dict = response.json()        # <class 'dict'>: {'genres': [{'id', 'name'}]}
#     genres= genres_dict['genres']

#     for genre in genres:
#         try: 
#             Genre.objects.get(id=genre.get('id'))
#         except:
#             Genre.objects.create(id=genre.get('id'), name=genre.get('name'))

#     url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=6f44898888940b2a302f0cdbee081d68&language=ko-KO&page=1&region=KR'
#     response = requests.get(url)
#     movie_dict = response.json()        # <class 'dict'>: {'page': 1, 'results': [{}]}
#     movies = movie_dict['results']

#     for movie in movies:

#         id = movie.get('id')

#         try:
#             Movie.objects.get(id=id)
#             continue

#         except:
#             m = Movie()
            
#             url_detail = f'https://api.themoviedb.org/3/movie/{id}?api_key=6f44898888940b2a302f0cdbee081d68&language=ko-KO'
#             response = requests.get(url_detail)
#             movie_detail = response.json()  # <class 'dict'>: {}

#             m.id = movie_detail.get('id')
#             m.title = movie_detail.get('title')
#             m.release_date = movie_detail.get('release_date')
#             m.country = movie_detail.get('production_countries')[0].get('name')
#             m.vote_count = movie_detail.get('vote_count')
#             m.vote_average = movie_detail.get('vote_average')
#             if movie_detail.get('overview'):
#                 m.overview = movie_detail.get('overview')
#             else:
#                 m.overview = ''
#             if movie_detail.get('poster_path'):
#                 m.poster_path = movie_detail.get('poster_path')
#             else:
#                 m.poster_path = ''
#             if movie_detail.get('backdrop_path'):
#                 m.backdrop_path = movie_detail.get('backdrop_path')
#             else:
#                 m.backdrop_path = ''


#             m.save()
#             m = Movie.objects.get(id=id)

#             genres = movie_detail.get('genres')
#             for genre in genres:
#                 # print(genre)
#                 m.genres.add(Genre.objects.get(id=genre['id']))
            
#             url_credits = f'https://api.themoviedb.org/3/movie/{id}/credits?api_key=6f44898888940b2a302f0cdbee081d68&language=ko-KO'
#             response = requests.get(url_credits)
#             movie_credits = response.json() # <class 'dict'>

#             casts = movie_credits['cast']

#             for cast in casts[:10]:
#                 try: 
#                     a = Actor.objects.get(id=cast.get('id'))
#                 except:
#                     if cast.get('profile_path'):
#                         a = Actor.objects.create(id=cast.get('id'), name=cast.get('name'), profile_path=cast.get('profile_path'))
#                     else:
#                         a = Actor.objects.create(id=cast.get('id'), name=cast.get('name'), profile_path='')
#                 m.actors.add(a)

#             directors = []
#             crews = movie_credits['crew']
#             for crew in crews:
#                 if crew['job'] == "Director":
#                     directors.append(crew)

#             for director in directors:
#                 try: 
#                     d = Director.objects.get(id=director.get('id'))
#                 except:
#                     if director.get('profile_path'):
#                         d = Director.objects.create(id=director.get('id'), name=director.get('name'), profile_path=director.get('profile_path'))
#                     else:
#                         d = Director.objects.create(id=director.get('id'), name=director.get('name'), profile_path='')

#                 m.directors.add(d)

