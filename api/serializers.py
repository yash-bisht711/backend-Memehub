from rest_framework import serializers
from .models import User_profile, Post, Comment


class UserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = User_profile
        fields = ['email', 'name', 'handle', 'profile_picture', 'avatar_url']

    def get_avatar_url(self, obj):
        return obj.avatar_url


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'timestamp', 'up_vote', 'down_vote']
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id', 'created_at']