from django.urls import path

urlpatterns = [
    path('posts/hot/<int:num>', admin.site.urls),
    path('posts/', include('movies.urls')),
    path('posts/<int:post_pk>/', include('community.urls')),
]