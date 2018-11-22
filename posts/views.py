from django.shortcuts import render

from posts.models import Post


def home(request):
    posts_list = Post.objects.all()
    a= "hola"
    b= "Adios"
    context = {'posts': [a, b]}
    return render(request, 'posts/home.html', context)
