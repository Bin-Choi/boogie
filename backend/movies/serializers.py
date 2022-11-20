from rest_framework import serializers
from .models import Movie, Actor, Director, Review, Genre, NowMovie, BoxOffice

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'

class GenreNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'id', 'poster_path', 'vote_average',)

class MovieNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title')

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    genres = GenreNameSerializer(many=True, read_only=True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)
    
    class Meta:
        model = Movie
        exclude = ('like_users',)

class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user')


class NowMovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NowMovie
        fields = '__all__'
        

class BoxOfficeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BoxOffice
        fields = '__all__'