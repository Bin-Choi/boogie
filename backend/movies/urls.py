from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:tmdb_id>', views.movie_detail),
    path('recent/<int:num>', views.movie_recent),
    path('reviews/recent/<int:num>', views.review_recent),
    # path('fill/data/', views.fill_data),
]
