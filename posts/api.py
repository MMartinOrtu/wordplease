from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostListSerializer, PostSerializer


class PostListAPIView(APIView):

     def get(self, request):
        posts= Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

     def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDetailAPIView(APIView):

     def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

     def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

     def delete(self, request, pk):
        ad = get_object_or_404(Post, pk=pk)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)