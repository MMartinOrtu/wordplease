from django.urls import path

from blogs.api import BlogsListAPIView, UserBlogAPIView
from blogs.views import BlogsListView, UserBlogView

urlpatterns = [
    path('blogs/<str:username>', UserBlogView.as_view(), name="user_blog"),
    path('blogs', BlogsListView.as_view(), name="blogs_list"),

    #API
    path('api/1.0/blogs/<int:id>/', UserBlogAPIView.as_view(), name='user_blog_api'),
    path('api/1.0/blogs/', BlogsListAPIView.as_view(), name='blogs_list_api')
]