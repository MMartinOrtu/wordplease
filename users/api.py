from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import UserPermission
from users.serializers import UserSerializer, UsersBlogsList


class CreateUserAPIView(CreateAPIView):

    serializer_class = UserSerializer


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]

class UsersBlogsListAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_list = []
        for user in users:
            users_list.append({
                'username': user.username,
                'blogURL': '{0}{1}{2}'.format(request._request._current_scheme_host, request._request.path, user.username )
            })
        serializer = UsersBlogsList(users_list, many=True)
        return Response(serializer.instance)
