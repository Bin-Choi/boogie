from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list),
    path('posts/hot/', views.post_list_hot),
    path('posts/<int:post_pk>/', views.post_detail),
    path('posts/<int:post_pk>/like/', views.post_like),
    path('posts/<int:post_pk>/comments/', views.comment_list),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/', views.
    comment_detail),
    path('posts/search/<str:query>/', views.search_post),
    
]