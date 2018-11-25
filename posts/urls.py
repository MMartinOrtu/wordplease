from django.urls import path

from posts.api import PostListAPIView, PostDetailAPIView
from posts.views import HomeView, PostDetailView, NewPostView

urlpatterns = [
    path('blogs/<str:username>/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('new-post', NewPostView.as_view(), name="new-post"),
    path('', HomeView.as_view(), name="home"),

    # API
    path('api/1.0/posts/', PostListAPIView.as_view(), name='post_list_api'),
    path('api/1.0/posts/<int:pk>', PostDetailAPIView.as_view(), name='post_detail_api')

]