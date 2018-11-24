from django.urls import path

from posts.views import HomeView, PostDetailView, NewPostView, UserPostsListView, BlogsListView

urlpatterns = [
    path('blogs/<str:username>/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('blogs/<str:username>/', UserPostsListView.as_view(), name="user_posts_list"),
    path('blogs', BlogsListView.as_view(), name="blog_list"),
    path('new-post', NewPostView.as_view(), name="new-post"),
    path('', HomeView.as_view(), name="home")
]