from django.urls import path
from posts.api import  UserPostsListAPIView
from users.api import UsersBlogsListAPIView
from blogs.views import UsersBlogsListView, UserBlogView

urlpatterns = [
    path('blogs/<str:username>', UserBlogView.as_view(), name="user_blog"),
    path('blogs', UsersBlogsListView.as_view(), name="blogs_list"),
    #API
    path('api/1.0/blogs/<str:username>', UserPostsListAPIView.as_view(), name='user_post_list_api'),
    path('api/1.0/blogs/', UsersBlogsListAPIView.as_view(), name='users_blogs_list_api')
]