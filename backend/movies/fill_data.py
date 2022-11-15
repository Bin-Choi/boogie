from django.shortcuts import render
import requests


# Create your views here.


url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=6f44898888940b2a302f0cdbee081d68&language=ko-KO&page=1&region=KR'

response = requests.get(url)

movie_dict = response.json()

print(movie_dict)

