"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts.views import HomeView, PostDetailView, NewPostView, UserPostsListView, BlogsListView
from users.views import LoginView, LogoutView, SignUpView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/<str:username>/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('blogs/<str:username>/', UserPostsListView.as_view(), name="user_posts_list"),
    path('blogs', BlogsListView.as_view(), name="blog_list"),
    path('new-post', NewPostView.as_view(), name="new-post"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('signup', SignUpView.as_view(), name='signup'),
    path('', HomeView.as_view(), name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
