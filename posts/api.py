from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
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


class UserPostsListAPIView(APIView):

    def get(self, request, username):
        posts = Post.objects.filter(owner__username=username)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
