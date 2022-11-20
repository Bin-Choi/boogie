from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.user_info),
    path('<int:user_pk>/follow/', views.follow),
    # path('fill/data/', views.fill_data),
]
