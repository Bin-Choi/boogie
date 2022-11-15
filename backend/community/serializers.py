from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import UserUsernameSerializer

class PostListSerializer(serializers.ModelSerializer):
    user = UserUsernameSerializer(many=True, read_only=True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'user')

class PostSerializer(serializers.ModelSerializer):
    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Post
        exclude =  ['like_users']
        read_only_fields = ('created_at', 'updated_at', 'user')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', 'user', 'created_at', 'original_comment', )