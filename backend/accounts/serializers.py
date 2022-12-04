from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserPreferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields =  ('adventure', 'fantasy', 'animation', 'drama', 'horror', 'action', 'comedy', 'history', 'western', 'thriller', 'crime', 'documentary', 'science_fiction', 'mystery', 'music', 'romance', 'family', 'war', 'tv_movie')

class UserListSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(use_url=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_image', )

class ProfileSeriallizer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(use_url=True)

    class Meta:
        model = get_user_model()
        fields = ('profile_image', )

class BackdropSeriallizer(serializers.ModelSerializer):
    backdrop_image = serializers.ImageField(use_url=True)

    class Meta:
        model = get_user_model()
        fields = ('backdrop_image', )