from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from django.views.generic import ListView

from blogs.models import Blog
from posts.models import Post


class UsersBlogsListView(ListView):
    model = User
    template_name = 'blogs/blogs_list.html'


class UserBlogView(View):

    def get(self, request, username):
        posts = Post.objects.select_related('owner') \
            .filter(owner__username=username, publication_date__lte=timezone.now()) \
            .exclude(status=Post.DRAFT).order_by('-last_modification')
        blog = Blog.objects.get(user__username=username)
        return render(request, 'blogs/user_blog.html', {'posts': posts, 'title': blog})
