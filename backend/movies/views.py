from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q

from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer, NowMovieSerializer, BoxOfficeSerializer
from .models import Movie, Actor, Genre, Director, Review, NowMovie, BoxOffice
import requests
from datetime import datetime ,timedelta

# Create your views here.
@api_view(['GET'])
def movie_detail(request, movie_pk):
    try:
        # movie = Movie.objects.get(pk=movie_pk)
        movie = Movie.objects.prefetch_related('actors', 'directors', 'genres', 'like_users').get(pk=movie_pk)
    except Movie.DoesNotExist:
        save_movie(movie_pk)
        movie = Movie.objects.prefetch_related('actors', 'directors', 'genres', 'like_users').get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
        is_liked = False
    else:
        movie.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return Response(context)

@api_view(['GET', 'POST'])
def review_list_movie(request, movie_pk):
    movie=Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie).order_by('-created_at')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST' and request.user.is_authenticated:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_review_movie(request, movie_pk):
    movie=Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        try: 
            review = Review.objects.get(movie=movie, user=request.user)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'DELETE':
        if review.user == request.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
        # elif request.method == 'GET':
        #     serializer = ReviewSerializer(Review)
        #     return Response(serializer.data)

        # elif request.method == 'PUT':
        #     serializer = ReviewSerializer(review, data=request.data)
        #     if serializer.is_valid(raise_exception=True):
        #         serializer.save()
        #         return Response(serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def review_list_recent(request):
    recent_reviews = Review.objects.all().order_by('created_at')[:5]

    serializer = ReviewSerializer(recent_reviews, many=True)
    print(type(serializer.data))
    return Response(serializer.data)

@api_view(['GET'])
def movie_list_now(request):
    now_show = NowMovie.objects.all()
    serializer = NowMovieSerializer(now_show, many=True)
    return Response(serializer.data)
     
@api_view(['GET'])     
def boxoffice(request):
    box_office = BoxOffice.objects.all().order_by('day')
    serializer = BoxOfficeSerializer(box_office, many=True)
    
    # 상위 5개 영화 제목 추출
    top5_title = []
    for topmovie in serializer.data[:5]:
        top5_title.append(topmovie['title'])
    
    # 데이터 가공
    data = {}
    for movie in serializer.data[5:]:
        if movie['title'] in top5_title:
            if not data.get(movie['title']):
                data[movie['title']] = [None, None, None, None, None, None, None]
                data[movie['title']][movie['day']] = movie['audi_cnt'] 
                continue
            data[movie['title']][movie['day']] = movie['audi_cnt'] 
    
    # chart.js 라이브러리에 맞게 가공
    chart_data = []
    for title in data:
        chart_data.append({"label":title, "data":data[title] })
    
    return Response(chart_data)

######################################################3

@api_view(['GET'])
def movie_recommend(request):
    movies = Movie.objects.prefetch_related('genres').all()

    for movie in movies:
        print(movie.genres.all().name)

    return Response({'data': 'data'})


######################################################3
@api_view(['GET'])
def review_list_user(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)

    if request.method == 'GET':
        reviews = Review.objects.filter(user=user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def review_list_recent(request):

    if request.method == 'GET':
        reviews = Review.objects.all().order_by('created_at')[:10]
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

######################################################3

def save_movie(id):
    m = Movie()
    
    url_detail = f'https://api.themoviedb.org/3/movie/{id}?api_key=6f44898888940b2a302f0cdbee081d68&language=ko-KO'
    response = requests.get(url_detail)
    movie_detail = response.json()  # <class 'dict'>: {}

    m.id = movie_detail.get('id')
    m.title = movie_detail.get('title')
    m.release_date = movie_detail.get('release_date')
    m.country = movie_detail.get('production_countries')[0].get('name')
    m.vote_count = movie_detail.get('vote_count')
    m.vote_average = movie_detail.get('vote_average')
    if movie_detail.get('overview'):
        m.overview = movie_detail.get('overview')
    else:
        m.overview = ''
    if movie_detail.get('poster_path'):
        m.poster_path = movie_detail.get('poster_path')
    else:
        m.poster_path = ''
    if movie_detail.get('backdrop_path'):
        m.backdrop_path = movie_detail.get('backdrop_path')
    else:
        m.backdrop_path = ''

    m.save()
    m = Movie.objects.get(id=id)

    genres = movie_detail.get('genres')
    for genre in genres:
        # print(genre)
        m.genres.add(Genre.objects.get(id=genre['id']))
    
    url_credits = f'https://api.themoviedb.org/3/movie/{id}/credits?api_key=6f44898888940b2a302f0cdbee081d68&language=ko-KO'
    response = requests.get(url_credits)
    movie_credits = response.json() # <class 'dict'>

    casts = movie_credits['cast']

    for cast in casts[:10]:
        try: 
            a = Actor.objects.get(id=cast.get('id'))
        except:
            if cast.get('profile_path'):
                a = Actor.objects.create(id=cast.get('id'), name=cast.get('name'), profile_path=cast.get('profile_path'))
            else:
                a = Actor.objects.create(id=cast.get('id'), name=cast.get('name'), profile_path='')
        m.actors.add(a)

    directors = []
    crews = movie_credits['crew']
    for crew in crews:
        if crew['job'] == "Director":
            directors.append(crew)

    for director in directors:
        try: 
            d = Director.objects.get(id=director.get('id'))
        except:
            if director.get('profile_path'):
                d = Director.objects.create(id=director.get('id'), name=director.get('name'), profile_path=director.get('profile_path'))
            else:
                d = Director.objects.create(id=director.get('id'), name=director.get('name'), profile_path='')

        m.directors.add(d)

def fill_movie_now_every_day():
    fill_movie_now()

def fill_movie_now():
    url = f'https://api.themoviedb.org/3/movie/now_playing?api_key=6f44898888940b2a302f0cdbee081d68&language=ko-KO&page=1&region=KR'
    response = requests.get(url)
    show_dict = response.json()

    now_show = NowMovie.objects.all()
    for movie in now_show:
        movie.delete()
    
    for movie in show_dict.get("results")[:10]:
        NowMovie.objects.create(id = movie['id'], title= movie["title"], vote_average = movie["vote_average"], poster_path = movie["poster_path"])
   
def fill_boxoffice_every_week():
    fill_boxoffice()

def fill_boxoffice():
    
    movies = BoxOffice.objects.all()
    for movie in movies:
        movie.delete()
    
    # 주간 박스오피스 요청 보내서 5개를 영화제목, 관객수, day=-1로 저장
    date = (datetime.now()-timedelta(days=7)).strftime('%Y%m%d')
    url = f'https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=128fedfc5557dcb90bba94cf5beff443&targetDt={date}&weekGb=0&itemPerPage=5'
    response = requests.get(url)
    boxoffice_dict = response.json()
            
    for movie in boxoffice_dict['boxOfficeResult']['weeklyBoxOfficeList']:
        BoxOffice.objects.create(title= movie['movieNm'], audi_cnt = movie['audiCnt'], day=-1)
    
    # 7일간의 일별 박스오피스
    for day_dif in range(7, 0, -1):
        date = (datetime.now()-timedelta(days=day_dif)).strftime('%Y%m%d')
        
        url = f'https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=128fedfc5557dcb90bba94cf5beff443&targetDt={date}&itemPerPage=10'
        response = requests.get(url)
        boxoffice_dict = response.json()
            
        for movie in boxoffice_dict['boxOfficeResult']['dailyBoxOfficeList']:
            BoxOffice.objects.create(title= movie['movieNm'], audi_cnt = movie['audiCnt'], day=7-day_dif)
     

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

