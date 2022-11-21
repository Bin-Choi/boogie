from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.user_info),
    path('<int:user_pk>/follow/', views.follow),
    path('<int:user_pk>/profile/', views.profile),
    path('<int:user_pk>/backdrop/', views.backdrop),
    # path('fill/data/', views.fill_data),
]
