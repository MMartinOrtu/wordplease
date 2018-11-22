from django.shortcuts import render

from posts.models import Post


def home(request):
    published_posts = Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')
    posts_list = published_posts[:5]
    context = {'posts': posts_list}
    return render(request, 'posts/home.html', context)
