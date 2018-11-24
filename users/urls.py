from django.urls import path

from users.api import CreateUserAPIView, UserDetailAPIView
from users.views import LoginView, LogoutView, SignUpView, UsersBlogsListView

urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('signup', SignUpView.as_view(), name='signup'),
    path('blogs', UsersBlogsListView.as_view(), name="users_blog_list"),

    #API
    path('api/1.0/users/', CreateUserAPIView.as_view(), name='create_user_api'),
    path('api/1.0/users/<int:pk>', UserDetailAPIView.as_view(), name='user_detail_api')
]