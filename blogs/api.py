from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import GenericAPIView, ListAPIView
from blogs.serializers import PostListSerializer, BlogsList
from blogs.models import Blog
from posts.models import Post


class BlogsListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsList
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['title']
    ordering_fields = ['title']


class UserBlogAPIView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['title', 'intro', 'body']
    ordering_fields = ['title', 'publication_date']

    def get_queryset(self):
        username = self.kwargs['username']
        posts_list = Post.objects.filter(owner__username=username).order_by('-publication_date')
        return posts_list if self.request.user.is_superuser or self.request.user.username == username \
            else posts_list.filter(status=Post.PUBLISHED)
