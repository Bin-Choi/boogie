# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from accounts.serializers import UserPreferenceSerializer
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer, NowMovieSerializer, BoxOfficeSerializer, MovieListGenreSerializer
from .models import Movie, Actor, Genre, Director, Review, NowMovie, BoxOffice

from datetime import datetime ,timedelta
import requests
from django.core.cache import cache


# API Keys
from django.conf import settings

TMDB_API_KEY = settings.TMDB_API_KEY
YOUTUBE_API_KEY = settings.YOUTUBE_API_KEY
KOFIC_API_KEY = settings.KOFIC_API_KEY
NAVER_CLIENT_ID = settings.NAVER_CLIENT_ID
NAVER_CLIENT_SECRET = settings.NAVER_CLIENT_SECRET

# Create your views here.
@api_view(['GET'])
def movie_detail_unlogin(request, movie_pk):
    try:
        # movie = Movie.objects.get(pk=movie_pk)
        movie = Movie.objects.prefetch_related('actors', 'directors', 'genres', 'like_users').get(pk=movie_pk)
    except Movie.DoesNotExist:
        save_movie(movie_pk)
        movie = Movie.objects.prefetch_related('actors', 'directors', 'genres', 'like_users').get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    data = serializer.data
    data['is_liked'] = False
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    try:
        # movie = Movie.objects.get(pk=movie_pk)
        movie = Movie.objects.prefetch_related('actors', 'directors', 'genres', 'like_users').get(pk=movie_pk)
    except Movie.DoesNotExist:
        save_movie(movie_pk)
        movie = Movie.objects.prefetch_related('actors', 'directors', 'genres', 'like_users').get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    if movie.like_users.filter(pk=request.user.pk).exists():
        is_liked = True
    else:
        is_liked = False
    data = serializer.data
    data['is_liked'] = is_liked
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    movie = Movie.objects.prefetch_related('genres').get(pk=movie_pk)
    # 장르 선호도 업데이트를 위한 준비
    user = get_user_model().objects.get(pk=request.user.pk)
    original_data = UserPreferenceSerializer(user).data
    genres = movie.genres.all()

    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
        is_liked = False
        # 유저의 장르선호도 업데이트
        for genre in genres:
            g = Genre.objects.get(pk=genre.id)
            original_data[g.field_name] -= 1
        updated_serializer = UserPreferenceSerializer(user, data=original_data)
        if updated_serializer.is_valid(raise_exception=True):
            updated_serializer.save()
    else:
        movie.like_users.add(request.user)
        is_liked = True
        # 유저의 장르선호도 업데이트
        for genre in genres:
            g = Genre.objects.get(pk=genre.id)
            original_data[g.field_name] += 1
        updated_serializer = UserPreferenceSerializer(user, data=original_data)
        if updated_serializer.is_valid(raise_exception=True):
            updated_serializer.save()
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
            # 리뷰 작성 시 점수 50점
            user = get_user_model().objects.get(pk=request.user.pk)
            user.score += 50
            user.save()

            # 장르 선호도 업데이트를 위한 준비
            user = get_user_model().objects.get(pk=request.user.pk)
            original_data = UserPreferenceSerializer(user).data
            genres = movie.genres.all()

            # 유저의 장르선호도 업데이트
            vote = request.data['vote'] - 3
            for genre in genres:
                g = Genre.objects.get(pk=genre.id)
                original_data[g.field_name] += vote
            updated_serializer = UserPreferenceSerializer(user, data=original_data)
            if updated_serializer.is_valid(raise_exception=True):
                updated_serializer.save()

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
def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    # 장르 선호도 업데이트를 위한 준비
    movie=Movie.objects.get(pk=movie_pk)
    user = get_user_model().objects.get(pk=request.user.pk)
    original_data = UserPreferenceSerializer(user).data
    genres = movie.genres.all()

    if request.method == 'DELETE':
        if review.user == request.user:
            review.delete()
            # 리뷰 삭제 시 점수 50점 차감
            user = get_user_model().objects.get(pk=request.user.pk)
            user.score -= 50
            user.save()

            # 유저의 장르선호도 업데이트(원래 점수로 초기화)
            vote = review.vote - 3
            for genre in genres:
                g = Genre.objects.get(pk=genre.id)
                original_data[g.field_name] -= vote
            updated_serializer = UserPreferenceSerializer(user, data=original_data)
            if updated_serializer.is_valid(raise_exception=True):
                updated_serializer.save()

            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def movie_list_related(request, movie_pk):
    # 기존 영화의 장르 리스트 가져오기
    movie = Movie.objects.get(pk=movie_pk)
    genre_list =  MovieListGenreSerializer(movie).data['genres']

    # 모든 영화를 장르 리스트 포함해서 가져오기
    serializer = MovieListGenreSerializer(Movie.objects.exclude(pk=movie_pk), many=True)
    movies = serializer.data

    # 장르 적합도를 보고 점수를 매겨 sort
    def calculate_score(movie):
        score = 0
        genres = movie['genres']
        for genre in genres:
            if genre in genre_list:
                score += 1
        return score
    movies.sort(key= lambda x: calculate_score(x), reverse=True)

    return Response(movies[:10])

@api_view(['GET'])
def video_list(request, movie_title):
    url = f'https://www.googleapis.com/youtube/v3/search'
    params = {
        'key': YOUTUBE_API_KEY,
        'part': 'id',
        'type': 'video',
        'maxResults': 5,
        'q': movie_title + ' 예고편',
    }
    response = requests.get(url, params=params)
    return Response(response.json())

@api_view(['GET'])
def tmdb_movie_list(request, query):
    url = f'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'ko-KO',
        'query': query,
    }
    response = requests.get(url, params=params)
    return Response(response.json())

@api_view(['GET'])
def review_list_recent(request):
    recent_reviews = Review.objects.all().order_by('-created_at')[:5]

    serializer = ReviewSerializer(recent_reviews, many=True)
    print(type(serializer.data))
    return Response(serializer.data)

@api_view(['GET'])
def movie_list_now(request):
    data = cache.get('now_movie')   # redis에서 캐싱된 데이터를 읽어온다
    return Response(data)

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

        chart_data.append({"label":title, "data":data[title]})
    
    return Response(chart_data)


@api_view(['GET'])
def search_naver(request, query):
    url = f'https://openapi.naver.com/v1/search/blog.json?query={query}'
    headers = {
    'Accept': 'application/json',
    'X-Naver-Client-Id': NAVER_CLIENT_ID,
    'X-Naver-Client-Secret': NAVER_CLIENT_SECRET,
    }
    response = requests.get(url, headers= headers)
    return Response(response.json())

@api_view(['GET'])
def movie_list_recommend_unlogin(request):
    movies = Movie.objects.all().order_by('-vote_average')[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list_recommend(request):
    # 유저의 장르 선호도 가져오기
    user = get_user_model().objects.get(pk=request.user.pk)
    genre_preference = UserPreferenceSerializer(user).data

    # 모든 영화를 장르 리스트 포함해서 가져오기
    serializer = MovieListGenreSerializer(Movie.objects.all(), many=True)
    movies = serializer.data

    # 선호도별 점수를 매겨 sort
    id_to_field_name = {12:	'adventure', 14: 'fantasy', 16:	'animation', 18	: 'drama', 27: 'horror', 28: 'action', 35: 'comedy', 36: 'history', 37:	'western', 53: 'thriller', 80: 'crime', 99: 'documentary', 878: 'science_fiction', 9648	: 'mystery', 10402: 'music', 10749: 'romance', 10751: 'family', 10752: 'war', 10770: 'tv_movie',}
    def calculate_score(movie):
        score = 0
        genres = movie['genres']
        for genre in genres:
            # field_name = Genre.objects.get(id=genre).field_name
            field_name = id_to_field_name[genre]
            score += genre_preference[field_name]
        return score
    movies.sort(key= lambda x: calculate_score(x), reverse=True)

    return Response(movies[:10])

#########################################이하는 Cron Job을 위한 함수###############################################

def save_movie(id):
    try:
        Movie.objects.get(id=id)
        return

    except:
        m = Movie()
    
        url_detail = f'https://api.themoviedb.org/3/movie/{id}?api_key={TMDB_API_KEY}&language=ko-KO'
        response = requests.get(url_detail)
        movie_detail = response.json()  # <class 'dict'>: {}

        m.id = movie_detail.get('id')
        m.title = movie_detail.get('title')
        m.release_date = movie_detail.get('release_date')
        if movie_detail.get('production_countries'):
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
        
        url_credits = f'https://api.themoviedb.org/3/movie/{id}/credits?api_key={TMDB_API_KEY}&language=ko-KO'
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
    url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=ko-KO&page=1&region=KR'
    response = requests.get(url)
    show_dict = response.json()

    # 10개의 영화 중 필요한 데이터만 뽑아서 가공
    data = []
    for movie in show_dict.get("results")[:10]:
        movie_data = {}
        movie_data["id"] = movie["id"]
        movie_data["title"] = movie["title"]
        movie_data["vote_average"] = movie["vote_average"]
        movie_data["poster_path"] = movie["poster_path"]
        data.append(movie_data)

    cache.set('now_movie', data)    # redis에 캐싱

def fill_boxoffice_every_week():
    fill_boxoffice()

def fill_boxoffice():
    
    movies = BoxOffice.objects.all()
    for movie in movies:
        movie.delete()
    
    # 주간 박스오피스 요청 보내서 5개를 영화제목, 관객수, day=-1로 저장
    date = (datetime.now()-timedelta(days=7)).strftime('%Y%m%d')
    url = f'https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={KOFIC_API_KEY}&targetDt={date}&weekGb=0&itemPerPage=5'
    response = requests.get(url)
    boxoffice_dict = response.json()
            
    for movie in boxoffice_dict['boxOfficeResult']['weeklyBoxOfficeList']:
        BoxOffice.objects.create(title= movie['movieNm'], audi_cnt = movie['audiCnt'], day=-1)
    
    # 7일간의 일별 박스오피스
    for day_dif in range(7, 0, -1):
        date = (datetime.now()-timedelta(days=day_dif)).strftime('%Y%m%d')
        
        url = f'https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={KOFIC_API_KEY}&targetDt={date}&itemPerPage=10'
        response = requests.get(url)
        boxoffice_dict = response.json()
            
        for movie in boxoffice_dict['boxOfficeResult']['dailyBoxOfficeList']:
            BoxOffice.objects.create(title= movie['movieNm'], audi_cnt = movie['audiCnt'], day=7-day_dif)

###################################이하는 초기 데이터를 API를 통해 채우기 위한 함수######################################

#################### Step2. Step1의 genre 채우는 거 실행한 다음에 한번만 더 실행해서 영어이름 채워줌###################
# def fill_genre_field_name(request):
#     url_genre = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=en-EN'
#     response = requests.get(url_genre)  # <class 'requests.models.Response'>: <Response [200]>
#     genres_dict = response.json()        # <class 'dict'>: {'genres': [{'id', 'name'}]}
#     genres= genres_dict['genres']

#     for genre in genres:
#         g = Genre.objects.get(id=genre.get('id'))
#         g.field_name = genre.get('name').lower().replace(' ','_')
#         g.save()
#######################################################################################################################


# def fill_data(request):
      #################### Step1. 이거는 한번만 실행하고 주석처리 ############################
#     # # genres
#     # url_genre = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KO'
#     # response = requests.get(url_genre)  # <class 'requests.models.Response'>: <Response [200]>
#     # genres_dict = response.json()        # <class 'dict'>: {'genres': [{'id', 'name'}]}
#     # genres= genres_dict['genres']

#     # for genre in genres:
#     #     try: 
#     #         Genre.objects.get(id=genre.get('id'))
#     #     except:
#     #         Genre.objects.create(id=genre.get('id'), name=genre.get('name'))
      #######################################################################################

#     for page in range(5, 11):
#         url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=ko-KO&page={page}&region=KR'
#         response = requests.get(url)
#         movie_dict = response.json()        # <class 'dict'>: {'page': 1, 'results': [{}]}
#         movies = movie_dict['results']

#         for movie in movies:

#             id = movie.get('id')

#             try:
#                 Movie.objects.get(id=id)
#                 continue

#             except:
#                 m = Movie()
                
#                 url_detail = f'https://api.themoviedb.org/3/movie/{id}?api_key={TMDB_API_KEY}&language=ko-KO'
#                 response = requests.get(url_detail)
#                 movie_detail = response.json()  # <class 'dict'>: {}

#                 m.id = movie_detail.get('id')
#                 m.title = movie_detail.get('title')
#                 m.release_date = movie_detail.get('release_date')
#                 m.country = movie_detail.get('production_countries')[0].get('name')
#                 m.vote_count = movie_detail.get('vote_count')
#                 m.vote_average = movie_detail.get('vote_average')
#                 if movie_detail.get('overview'):
#                     m.overview = movie_detail.get('overview')
#                 else:
#                     m.overview = ''
#                 if movie_detail.get('poster_path'):
#                     m.poster_path = movie_detail.get('poster_path')
#                 else:
#                     m.poster_path = ''
#                 if movie_detail.get('backdrop_path'):
#                     m.backdrop_path = movie_detail.get('backdrop_path')
#                 else:
#                     m.backdrop_path = ''


#                 m.save()
#                 m = Movie.objects.get(id=id)

#                 genres = movie_detail.get('genres')
#                 for genre in genres:
#                     # print(genre)
#                     m.genres.add(Genre.objects.get(id=genre['id']))
                
#                 url_credits = f'https://api.themoviedb.org/3/movie/{id}/credits?api_key={TMDB_API_KEY}&language=ko-KO'
#                 response = requests.get(url_credits)
#                 movie_credits = response.json() # <class 'dict'>

#                 casts = movie_credits['cast']

#                 for cast in casts[:10]:
#                     try: 
#                         a = Actor.objects.get(id=cast.get('id'))
#                     except:
#                         if cast.get('profile_path'):
#                             a = Actor.objects.create(id=cast.get('id'), name=cast.get('name'), profile_path=cast.get('profile_path'))
#                         else:
#                             a = Actor.objects.create(id=cast.get('id'), name=cast.get('name'), profile_path='')
#                     m.actors.add(a)

#                 directors = []
#                 crews = movie_credits['crew']
#                 for crew in crews:
#                     if crew['job'] == "Director":
#                         directors.append(crew)

#                 for director in directors:
#                     try: 
#                         d = Director.objects.get(id=director.get('id'))
#                     except:
#                         if director.get('profile_path'):
#                             d = Director.objects.create(id=director.get('id'), name=director.get('name'), profile_path=director.get('profile_path'))
#                         else:
#                             d = Director.objects.create(id=director.get('id'), name=director.get('name'), profile_path='')

#                     m.directors.add(d)

