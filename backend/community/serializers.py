from rest_framework import serializers
from .models import Post, Comment

class PostListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'username', 'like_users_count')
        # fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Post
        exclude =  ['like_users',]
        read_only_fields = ('user',)

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', 'user', 'original_comment', )