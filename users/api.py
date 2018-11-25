from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from users.permissions import UserPermission
from users.serializers import UserSerializer


class CreateUserAPIView(CreateAPIView):

    serializer_class = UserSerializer


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
