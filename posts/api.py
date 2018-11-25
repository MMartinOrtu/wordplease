from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.permissions import PostPermission, BlogPermission
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


class UserPostsListAPIView(APIView):

    #permission_classes = [isAdminUser]

    def get(self, request, username):
        posts_list = Post.objects.filter(owner__username=username)
        if request.user.is_superuser or request.user.username == username:
            queryset = posts_list
        else:
            queryset = posts_list.filter(status=Post.PUBLISHED)

        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)
