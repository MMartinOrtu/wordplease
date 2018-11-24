from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        return view.action in ('list', 'retrieve') or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # define si el usuario autenticado puede realizar la acción sobre el objeto obj
        return view.action == 'retrieve' or obj.owner == request.user or request.user.is_superuser
    