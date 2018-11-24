from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        from users.api import UserDetailAPIView
        return request.method == 'POST' or request.user.is_superuser or isinstance(view, UserDetailAPIView)

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj
