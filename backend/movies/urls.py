from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.movie_detail),
    path('recent/<int:num>/', views.movie_recent),
    path('reviews/user/', views.review_list_user),
    path('reviews/movie/<int:movie_pk>/', views.review_list_movie),
    path('reviews/recent/<int:num>/', views.review_list_recent),
    path('reviews/<int:pk>/', views.delete_review),
    # path('fill/data/', views.fill_data),
]
