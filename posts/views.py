from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from posts.forms import NewPostForm
from posts.models import Post


class HomeView(View):

    def get(self, request):
        published_posts = Post.objects.select_related('owner').filter(status=Post.PUBLISHED).order_by('-last_modification')
        posts_list = published_posts[:5]
        context = {'posts': posts_list}
        return render(request, 'posts/home.html', context)



class PostDetailView(View):

    def post_detail(self, request, username, post_pk):
        try:
            post = Post.objects.select_related('owner').get(pk=post_pk)
            context = {'post': post}
            return render(request, 'posts/post_detail.html', context)
        except Post.DoesNotExist:
            return HttpResponse('Post not found', status=404)


class NewPostView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = NewPostForm()
        return render(request, 'posts/new_post.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        new_post = Post(owner=request.user)
        form = NewPostForm(request.POST, request.FILES, instance=new_post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post {0} created successfully!'.format(new_post.name))
            form = NewPostForm()
        return render(request, 'posts/new_post.html', {'form': form})
