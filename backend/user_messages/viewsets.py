from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from user_messages.models import UserMessage
from user_messages.permissions import UserMessagePermission
from user_messages.serializers import (
    UserMessageCreateSerializer,
    UserMessageListSerializer,
    UserMessageUpdateSerializer,
)


@extend_schema(tags=["Сообщения"])
class UserMessageViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    authentication_classes = [BasicAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated, UserMessagePermission]

    def get_queryset(self):
        queryset = UserMessage.objects.select_related("created_by")
        return queryset

    def get_serializer_class(self):
        serializer_class = UserMessageListSerializer
        if self.action == self.create.__name__:
            serializer_class = UserMessageCreateSerializer
        elif self.action == self.partial_update.__name__:
            serializer_class = UserMessageUpdateSerializer
        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        self.add_created_by(instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        instance: UserMessage = serializer.save()
        return instance

    def add_created_by(self, instance):
        instance.created_by = self.request.user
        instance.save()
        return instance
