from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post


def home(request):
    published_posts = Post.objects.select_related('owner').filter(status=Post.PUBLISHED).order_by('-last_modification')
    posts_list = published_posts[:5]
    context = {'posts': posts_list}
    return render(request, 'posts/home.html', context)


def post_detail(request, username, post_pk):
    try:
        post = Post.objects.get(pk=post_pk)
        context = {'post': post}
        return render(request, 'posts/post_detail.html', context)
    except Post.DoesNotExist:
        return HttpResponse('Post not found', status=404)
