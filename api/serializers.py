from rest_framework import serializers
from .models import User_profile

class UserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = User_profile
        fields = ['email', 'name', 'handle', 'profile_picture', 'avatar_url']

    def get_avatar_url(self, obj):
        return obj.avatar_url
