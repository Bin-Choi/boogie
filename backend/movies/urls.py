from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/<int:tmdb_id>', views.movie_detail),
    path('recent/<int:num>', views.movie_recent),
    path('reviews/recent/<int:num>', views.review_recent)
]
