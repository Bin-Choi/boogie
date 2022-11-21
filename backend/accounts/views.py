from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Prefetch

from .serializers import ProfileSeriallizer, BackdropSeriallizer
from community.serializers import PostListSerializer, CommentPostSerializer
from community.models import Comment
from movies.serializers import MovieListSerializer, ReviewSerializer, MovieSerializer, MovieGenreSerializer
from movies.models import Movie, Review

from collections import defaultdict
# Create your views here.
@api_view(['GET'])
def user_info(request, username):
    if request.method == 'GET':
        User = get_user_model()

        # Step1. 필요한 정보 일단 다 생성해서 보내기
        user = User.objects.prefetch_related(
            'followings', 'followers',
            'post_set', 'like_posts',
            # Prefetch('comment_set',  queryset=Review.objects.select_related('post')),
            Prefetch('like_movies', queryset=Movie.objects.prefetch_related('genres')),
            'review_set',
        ).get(username=username)

        data = {
            'id': user.id,
            'username': user.username,
            'date_joined': user.date_joined,
            'score': user.score,
            'profile_image': ProfileSeriallizer(user).data,
            'backdrop_image': BackdropSeriallizer(user).data,
            'followings': [{following.username, following.id}  for following in user.followings.all()],
            'followers': [{follower.username, follower.id} for follower in user.followers.all()],
            'my_posts': PostListSerializer(user.post_set.all(), many=True).data,
            'like_posts': PostListSerializer(user.like_posts.all(), many=True).data,
            'like_movies': MovieListSerializer(user.like_movies.all(), many=True).data,
            'my_reviews': ReviewSerializer(user.review_set.all(), many=True).data,
        }

        # Step2. 취향 장르 분석. review로 보완 필요
        # print(user.like_movies.all().genres)
        genre_preference = defaultdict(int)
        movies_genres = MovieGenreSerializer(user.like_movies.all(), many=True).data
        for genres in movies_genres:
            for genre in genres['genres']:
                genre_preference[genre['name']] += 1

        data['genre_preference'] = genre_preference

        return Response(data) 
    # # like_movies: MovieList, 근데 장르가 필요
    # user = User.objects.prefetch_related(
    #     Prefetch('review_set',  queryset=Review.objects.select_related('movie')),
    #     Prefetch('like_movies', queryset=Movie.objects.prefetch_related('genres'))
    # ).get(username=username)
    
    # data = {
    #     # 'reviews': MovieSerializer(user.review_set.movie, many=True).data,
    #     'like_movies': MovieGenreSerializer(user.like_movies.all(), many=True).data,
    #     }

    # return Response(data) 
    # user = User.objects.prefetch_related(
    #     'followings', 'followers', 'post_set', 'like_posts', 'comment_set', 'like_movies', 'like_movies__genres', 'review_set',).get(username=username)
    #     # 'followings', 'followers', 'post_set', 'like_posts','comment_set__po', 'review_set',).get(username=username)
        
    # # 팔로잉, 팔로워
    # # 내가 쓴 글
    # # 내가 좋아요 한 글
    # # 내가 댓글 단 글
    # # 내가 쓴 리뷰
    # # 내가 찜한 영화
    
    # data = {
    #     'id': user.id,
    #     'username': user.username,
    #     'date_joined': user.date_joined,
    #     'score': user.score,
    #     'followings': [{following.username, following.id}  for following in user.followings.all()],
    #     'followers': [{follower.username, follower.id} for follower in user.followers.all()],
    #     'my_posts': PostListSerializer(user.post_set.all(), many=True).data,
    #     'like_posts': PostListSerializer(user.like_posts.all(), many=True).data,
    #     # 'commented_posts': PostListSerializer(user.comment_set.post., many=True).data,
    #     # 'like_movies': MovieListSerializer(user.like_movies.all(), many=True).data,
    #     'like_movies_genres': [genre.id for genre in user.like_movies.genres.all()],
    #     'my_reviews': ReviewSerializer(user.review_set.all(), many=True).data,
    #     }

    # return Response(data) 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):

    if request.method == 'POST':
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            data = {
                'is_followed': is_followed,
            }
            return Response(data)
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def profile(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)

    if user == request.user:
        if request.method == 'PUT':
            serializer = ProfileSeriallizer(user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['PUT', 'DELETE'])
def backdrop(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)

    if user == request.user:
        if request.method == 'PUT':
            serializer = BackdropSeriallizer(user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    return Response(status=status.HTTP_403_FORBIDDEN)