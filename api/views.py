from rest_framework import viewsets
from .models import User_profile
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User_profile.objects.all()
    serializer_class = UserSerializer