from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import User_profile, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User_profile.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['get'], url_path='by-user/(?P<email>.+)')
    def get_user_by_email(self, request, email=None):
        """Get User by Email"""
        user = get_object_or_404(User_profile, email=email)
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-timestamp')
    serializer_class = PostSerializer
    

    @action(detail=False, methods=['get'])
    def new(self, request):
        """Sort by newest posts"""
        posts = Post.objects.all().order_by('-timestamp')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def top_day(self, request):
        """Top posts in last 24 hours"""
        day_ago = timezone.now() - timedelta(days=1)
        posts = Post.objects.filter(timestamp__gte=day_ago).order_by('-up_vote')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def top_week(self, request):
        """Top posts this week"""
        week_ago = timezone.now() - timedelta(days=7)
        posts = Post.objects.filter(timestamp__gte=week_ago).order_by('-up_vote')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def top_all(self, request):
        """Top posts of all time"""
        posts = Post.objects.all().order_by('-up_vote')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='by-id/(?P<post_id>[^/.]+)')
    def get_post_by_id(self, request, post_id=None):
        """Get post by UUID"""
        post = get_object_or_404(Post, id=post_id)
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='by-user/(?P<email>.+)')
    def get_posts_by_user(self, request, email=None):
        """Get posts created by a user (by email)"""
        user = get_object_or_404(User_profile, email=email)
        posts = Post.objects.filter(created_by=user).order_by('-timestamp')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    
    @action(detail=False, methods=['get'], url_path=r'by-post/(?P<post_id>[0-9a-f-]+)')
    def get_comments_by_post(self, request, post_id=None):
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post).order_by('-created_at')
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)