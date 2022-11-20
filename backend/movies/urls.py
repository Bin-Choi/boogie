from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.movie_detail),
    path('recent/<int:num>/', views.movie_recent),
    path('reviews/user/', views.review_list_user),
    path('reviews/movie/<int:movie_pk>/', views.review_list_movie),
    path('reviews/recent/', views.review_list_recent),
    path('reviews/<int:pk>/', views.delete_review),
    path('reviews/', views.review_list_recent),
    path('show/', views.movie_show),
    path('boxoffice/', views.boxoffice),
    # path('fill/', views.fill_boxoffice)
    # path('fill/data/', views.fill_data),
]
