from rest_framework import serializers
from .models import User_profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_profile
        fields = '__all__'