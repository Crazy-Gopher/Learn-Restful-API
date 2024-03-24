from rest_framework import viewsets, permissions
from user.serializers import UserSerilizer
from user.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerilizer
    # permission_classes = [permissions.IsAuthenticated]