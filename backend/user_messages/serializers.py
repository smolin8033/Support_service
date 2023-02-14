from rest_framework.serializers import ModelSerializer

from user_messages.models import UserMessage
from users.serializers import UserDetailSerializer


class UserMessageDetailSerializer(ModelSerializer):
    class Meta:
        model = UserMessage
        fields = ("id", "text", "created_by", "created_at")


class UserMessageListSerializer(ModelSerializer):
    created_by = UserDetailSerializer()

    class Meta:
        model = UserMessage
        fields = ("id", "text", "created_by", "created_at")


class UserMessageCreateSerializer(ModelSerializer):
    class Meta:
        model = UserMessage
        fields = ("text", "ticket")


class UserMessageUpdateSerializer(ModelSerializer):
    class Meta:
        model = UserMessage
        fields = ("text",)
