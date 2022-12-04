# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from operator import itemgetter
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Post, Comment
from .serializers import PostSerializer, PostListSerializer, CommentSerializer


# Create your views here.
@api_view(['GET'])
def post_list_hot(request):
    hot_posts = Post.objects.all()[:5]
    serializer = PostListSerializer(hot_posts, many=True)
    data = sorted(serializer.data, key=itemgetter('like_users_count'), reverse=True)
    return Response(data)

@api_view(['GET'])
def search_post(request, query):
    posts = Post.objects.filter(Q(title__contains=query) | Q(content__contains=query))
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                # 게시글 작성 시 점수 100점
                user = get_user_model().objects.get(pk=request.user.pk)
                user.score += 100
                user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def post_detail_unlogin(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        data = serializer.data
        data['is_liked'] = False
        return Response(data)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        if post.like_users.filter(pk=request.user.pk).exists():
            is_liked = True
        else:
            is_liked = False
        data = serializer.data
        data['is_liked'] = is_liked
        return Response(data)
    
    elif request.method == 'DELETE':
        if post.user == request.user:
            post.delete()
            # 게시글 삭제 시 점수 100점 차감
            user = get_user_model().objects.get(pk=request.user.pk)
            user.score -= 100
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'PUT':
        if post.user == request.user:
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if post.like_users.filter(pk=request.user.pk).exists():
        post.like_users.remove(request.user)
        is_liked = False
    else:
        post.like_users.add(request.user)
        is_liked = True
    data = {
        'is_liked': is_liked,
    }
    return Response(data)
    
        
@api_view(['GET', 'POST'])
def comment_list(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'GET':
        comments = Comment.objects.filter(post=post).order_by('created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST' and request.user.is_authenticated:
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, post=post)
            # 댓글 작성 시 점수 10점
            user = get_user_model().objects.get(pk=request.user.pk)
            user.score += 10
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST', 'GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'POST':    # 대댓글 생성
        post = get_object_or_404(Post, pk=post_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, post=post, original_comment=comment)
            # 댓글 작성 시 점수 10점
            user = get_user_model().objects.get(pk=request.user.pk)
            user.score += 10
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        if comment.user == request.user:
            comment.delete()
            # 댓글 삭제 시 점수 10점 차감
            user = get_user_model().objects.get(pk=request.user.pk)
            user.score -= 10
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

    # elif request.method == 'PUT':
    #     serializer = CommentSerializer(comment, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)

    # elif request.method == 'GET':
    #     serializer = CommentSerializer(comment)
    #     return Response(serializer.data)