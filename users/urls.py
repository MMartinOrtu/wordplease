from django.urls import path

from users.api import CreateUserAPIView, UserDetailAPIView, UsersBlogsListAPIView
from users.views import LoginView, LogoutView, SignUpView

urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('signup', SignUpView.as_view(), name='signup'),

    #API
    path('api/1.0/blogs/', UsersBlogsListAPIView.as_view(), name='users_blogs_list_api'),
    path('api/1.0/users/', CreateUserAPIView.as_view(), name='create_user_api'),
    path('api/1.0/users/<int:pk>', UserDetailAPIView.as_view(), name='user_detail_api')
]