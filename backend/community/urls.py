from django.urls import path
from . import views

urlpatterns = [
    path('posts/hot/<int:num>/', views.post_list_hot),
    path('posts/', views.post_list),
    path('posts/<int:post_pk>/', views.post_detail),
    path('comments/post/<int:post_pk>/', views.comment_list),
    path('comments/post/<int:post_pk>/comment/<int:comment_pk>/', views.recomment_list)
]