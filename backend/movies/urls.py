from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/unlogin/', views.movie_detail_unlogin),
    path('<int:movie_pk>/like/', views.movie_like),
    path('<int:movie_pk>/reviews/', views.review_list_movie),
    path('<int:movie_pk>/myreview/', views.my_review_movie),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail),
    path('<int:movie_pk>/related/', views.movie_list_related),
    path('<str:movie_title>/videos/', views.video_list),
    path('<str:query>/tmdb/', views.tmdb_movie_list),
    path('reviews/recent/', views.review_list_recent),
    path('now/', views.movie_list_now),
    path('boxoffice/', views.boxoffice),
    path('recommend/', views.movie_list_recommend),
    path('recommend/unlogin/', views.movie_list_recommend_unlogin),
    path('naver/<str:query>/', views.search_naver),

    # path('fill/now/', views.fill_movie_now),
    # path('fill/boxoffice/', views.fill_boxoffice),
    # path('fill/data/', views.fill_data),
    # path('fill/genre/', views.fill_genre_field_name),
]
