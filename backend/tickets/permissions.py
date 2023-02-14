from rest_framework.permissions import BasePermission


class TicketPermission(BasePermission):
    """
    Пермишионы для поддержки, саппорт и
    для клиентов, кастомеров
    """

    def has_permission(self, request, view):
        if request.user.role == "S":
            if view.action in ["list", "retrieve", "partial_update"]:
                return True
            elif view.action in ["create", "destroy"]:
                return False

        elif request.user.role == "C":
            if view.action in ["create", "destroy", "list", "retrieve"]:
                return True
            elif view.action == "partial_update":
                return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == "C":
            if view.action in ["create"]:
                return True
            elif view.action in ["retrieve", "destroy"]:
                return obj.created_by == request.user
            else:
                return False
        return True
