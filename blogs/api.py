from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import GenericAPIView

from blogs.models import Blog
from blogs.serializers import BlogsList, PostListSerializer
from posts.models import Post


class BlogsListAPIView(GenericAPIView):
    queryset = Blog.objects.all()
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['username']
    ordering_fields = ['username']

    def get(self, request):
        users = Blog.objects.all()
        users_list = []
        for user in users:
            users_list.append({
                'username': user.username,
                'blogURL': '{0}{1}{2}'.format(request._request._current_scheme_host, request._request.path, user.username )
            })
        queryset = self.paginate_queryset(users_list)
        serializer = BlogsList(queryset, many=True)
        return self.get_paginated_response(serializer.instance)


class UserBlogAPIView(GenericAPIView):
    queryset = []

    def get(self, request, username):
        posts_list = Post.objects.filter(owner__username=username).order_by('-publication_date')
        if request.user.is_superuser or request.user.username == username:
            queryset = self.paginate_queryset(posts_list)
        else:
            queryset = self.paginate_queryset(posts_list.filter(status=Post.PUBLISHED))

        serializer = PostListSerializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)
