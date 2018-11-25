from django.contrib.auth.models import User
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
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


class UsersBlogsListAPIView(GenericAPIView):
    queryset = User.objects.all()
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['username']
    ordering_fields = ['username']

    def get(self, request):
        users = User.objects.all()
        users_list = []
        for user in users:
            users_list.append({
                'username': user.username,
                'blogURL': '{0}{1}{2}'.format(request._request._current_scheme_host, request._request.path, user.username )
            })
        queryset = self.paginate_queryset(users_list)
        serializer = UsersBlogsList(queryset, many=True)
        return self.get_paginated_response(serializer.instance)
