from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Director(models.Model):
    tmdb_id = models.IntegerField()
    name = models.CharField(max_length= 30)
    profile_path = models.CharField(max_length=200, blank=True)

class Actor(models.Model):
    tmdb_id = models.IntegerField()
    name = models.CharField(max_length = 30)
    profile_path = models.CharField(max_length=200, blank=True)

class Genre(models.Model):
    tmdb_id = models.IntegerField()
    name = models.CharField(max_length = 30)

class Movie(models.Model):
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=128)
    release_date = models.DateField()
    country = models.CharField(max_length=30)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField(blank=True)
    poster_path = models.CharField(max_length=200, blank=True)
    backdrop_path = models.CharField(max_length=200, blank=True)
    actors = models.ManyToManyField(Actor, related_name = "movies")
    genres = models.ManyToManyField(Genre, related_name = "movies")
    directors = models.ManyToManyField(Director, related_name = "movies")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "like_movies")

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    content = models.TextField(blank=True)
    vote = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

