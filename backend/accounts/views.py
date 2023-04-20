# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from django.db.models import Prefetch

from movies.models import Movie, Genre
from movies.serializers import MovieListSerializer, ReviewSerializer
from community.serializers import PostListSerializer
from .serializers import ProfileSeriallizer, BackdropSeriallizer, UserListSerializer, UserPreferenceSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request, username):
    if request.method == 'GET':
        User = get_user_model()

        # Step1. 필요한 정보 일단 다 가져오기
        user = User.objects.prefetch_related(
            'followings', 'followers',
            'post_set', 'like_posts',
            # Prefetch('comment_set',  queryset=Review.objects.select_related('post')),
            Prefetch('like_movies', queryset=Movie.objects.prefetch_related('genres')),
            'review_set',
        ).get(username=username)

        # Step2. 팔로잉 정보 계산
        followers = user.followers.all()
        if request.user in followers:
            is_followed = True
        else:
            is_followed = False

        # Step3. 취향장르 TOP3 출력
        genre_preference = []
        preference_data = UserPreferenceSerializer(user).data
        for genre in preference_data:
            if preference_data[genre] > 0:
                genre_preference.append({'genre': Genre.objects.get(field_name=genre).name, 'score': preference_data[genre]})
        genre_preference = sorted(genre_preference, key= lambda x: x['score'], reverse=True)[:3]

        data = {
            'id': user.id,
            'username': user.username,
            'date_joined': user.date_joined,
            'score': user.score,
            'genre_preference': genre_preference,
            'profile_image': ProfileSeriallizer(user).data['profile_image'],
            'backdrop_image': BackdropSeriallizer(user).data['backdrop_image'],
            'followings': UserListSerializer(user.followings.all(), many=True).data,
            'followers': UserListSerializer(followers, many=True).data,
            'my_posts': PostListSerializer(user.post_set.all(), many=True).data,
            'like_posts': PostListSerializer(user.like_posts.all(), many=True).data,
            'like_movies': MovieListSerializer(user.like_movies.all(), many=True).data,
            'my_reviews': ReviewSerializer(user.review_set.all(), many=True).data,
            'is_followed': is_followed
        }

        return Response(data)

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
                print(str(you.followers.add(me)))
                is_followed = True
            data = {
                'is_followed': is_followed,
            }
            return Response(data)
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['PUT', 'DELETE'])
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

        if request.method== 'DELETE':
            default_profile = 'profile/default.png'
            user.profile_image = default_profile
            user.save()
            return Response({'profile_image': '/media/' + default_profile})
    return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def backdrop(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)

    if user == request.user:
        if request.method == 'PUT':
            serializer = BackdropSeriallizer(user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

        if request.method== 'DELETE':
            default_backdrop = 'backdrop/default.jpg'
            user.profile_image = default_backdrop
            user.save()
            return Response({'backdrop_image': '/media/' + default_backdrop})
    return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def withdraw(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)

    if user == request.user:
        if request.method== 'DELETE':
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_403_FORBIDDEN)