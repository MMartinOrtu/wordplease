from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView
from posts.forms import NewPostForm
from posts.models import Post


class HomeView(ListView):

    queryset = Post.objects.select_related('owner').filter(publication_date__lte=datetime.now())\
            .exclude(status=Post.DRAFT).order_by('-last_modification')
    template_name = 'posts/home.html'


class PostDetailView(DetailView):

    model=Post
    template_name = 'posts/post_detail.html'


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
            messages.success(request, 'Post {0} created successfully!'.format(new_post.title))
            form = NewPostForm()
        return render(request, 'posts/new_post.html', {'form': form})


class UserPostsListView(ListView):
    template_name = 'posts/home.html'

    def get_queryset(self):
        username = self.kwargs['username']
        return Post.objects.select_related('owner')\
            .filter(owner__username=username, publication_date__lte=datetime.now())\
            .exclude(status=Post.DRAFT).order_by('-last_modification')
