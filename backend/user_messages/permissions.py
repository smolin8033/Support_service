from rest_framework.permissions import BasePermission


class UserMessagePermission(BasePermission):
    """
    Общие пермишионы и для поддержки, и для кастомеров.
    Работает CRUD только своих сообщений
    """

    def has_permission(self, request, view):
        if request.user.role in ["S", "C"]:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.role in ["S", "C"]:
            return obj.created_by == request.user
