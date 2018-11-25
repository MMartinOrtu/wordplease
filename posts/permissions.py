from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated or request.method == 'GET'

    def has_object_permission(self, request, view, obj):
        return request.method == 'GET' or obj.owner == request.user or request.user.is_superuser
