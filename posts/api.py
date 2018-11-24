from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostListSerializer, PostSerializer


class PostListAPIView(ListCreateAPIView):

    queryset = Post.objects.all()

    def get_serializer_class(self):
        return PostListSerializer if self.request.method == 'GET' else PostSerializer


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

 # class UserPostsListAPIView(ListAPIView):

     #queryset = Post.objects.filter(owner__username=username)
    # serializer_class = PostListSerializer


class UserPostsListAPIView(APIView):

    def get(self, request, username):
        posts = Post.objects.filter(owner__username=username)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
