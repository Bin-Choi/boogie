from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/like/', views.movie_like),
    path('<int:movie_pk>/reviews/', views.review_list_movie),
    path('<int:movie_pk>/myreview/', views.my_review_movie),
    path('users/<int:user_pk>/reviews/', views.review_list_user),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/recent/', views.review_list_recent),
    path('now/', views.movie_list_now),
    path('boxoffice/', views.boxoffice),
    path('recommend/', views.movie_recommend),
    # path('fill/now/', views.fill_movie_now),
    # path('fill/boxoffice/', views.fill_boxoffice),
    # path('fill/data/', views.fill_data),
]
