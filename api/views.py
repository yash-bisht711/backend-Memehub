from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import User_profile, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User_profile.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Optionally filter users by query params like `email`.
        Example: GET /api/users/?email=<email>
        """
        queryset = User_profile.objects.all()

        email = self.request.query_params.get('email')
        if email:
            queryset = queryset.filter(email=email)

        return queryset

    def list(self, request, *args, **kwargs):
        """
        List all users or filter by query parameters like `email`.
        Example: GET /api/users/?email=<email>
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Get user by ID (UUID)
        """
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Create a new user
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update a user by its ID (UUID)
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a user by its ID (UUID)
        """
        return super().destroy(request, *args, **kwargs)
    

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-timestamp')
    serializer_class = PostSerializer

    def get_queryset(self):
        """
        Optionally filter the posts using query parameters:
        - ?new=true
        - ?top_day=true
        - ?top_week=true
        - ?top_all=true
        - ?user_email=<email>
        """
        queryset = Post.objects.all()

        # Newest posts (default order)
        if self.request.query_params.get('new') == 'true':
            return queryset.order_by('-timestamp')

        # Top posts in last 24 hours
        if self.request.query_params.get('top_day') == 'true':
            day_ago = timezone.now() - timedelta(days=1)
            return queryset.filter(timestamp__gte=day_ago).order_by('-up_vote')

        # Top posts this week
        if self.request.query_params.get('top_week') == 'true':
            week_ago = timezone.now() - timedelta(days=7)
            return queryset.filter(timestamp__gte=week_ago).order_by('-up_vote')

        # Top posts of all time
        if self.request.query_params.get('top_all') == 'true':
            return queryset.order_by('-up_vote')

        # Posts by user
        email = self.request.query_params.get('user_email')
        if email:
            user = get_object_or_404(User_profile, email=email)
            return queryset.filter(created_by=user).order_by('-timestamp')

        return queryset.order_by('-timestamp')

    def update(self, request, *args, **kwargs):
        """
        Standard PUT/PATCH endpoint at /posts/<id>/
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Standard DELETE endpoint at /posts/<id>/
        """
        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Standard GET /posts/<id>/ to get a single post
        """
        return super().retrieve(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        Optionally filter comments by post_id via query parameter.
        Example: GET /api/comments/?post_id=<post_id>
        """
        queryset = Comment.objects.all()

        post_id = self.request.query_params.get('post_id')
        if post_id:
            post = get_object_or_404(Post, id=post_id)
            queryset = queryset.filter(post=post)

        return queryset

    def retrieve(self, request, *args, **kwargs):
        """
        Standard GET /comments/<id>/ to get a single comment
        """
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Standard POST /comments/ to create a new comment
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Standard PUT/PATCH /comments/<id>/ to update a comment
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Standard DELETE /comments/<id>/ to delete a comment
        """
        return super().destroy(request, *args, **kwargs)