from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostListSerializer, PostSerializer


class PostListAPIView(ListCreateAPIView):

    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]


class UserPostsListAPIView(GenericAPIView):
    queryset = []

    def get(self, request, username):
        posts_list = Post.objects.filter(owner__username=username).order_by('-publication_date')
        if request.user.is_superuser or request.user.username == username:
            queryset = self.paginate_queryset(posts_list)
        else:
            queryset = self.paginate_queryset(posts_list.filter(status=Post.PUBLISHED))

        serializer = PostListSerializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)
