from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import User_profile, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User_profile.objects.all()
    serializer_class = UserSerializer
    

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


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer