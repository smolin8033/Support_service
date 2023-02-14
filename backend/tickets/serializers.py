from rest_framework.serializers import ModelSerializer

from tickets.models import Ticket
from user_messages.serializers import UserMessageDetailSerializer
from users.serializers import UserDetailSerializer


class TicketCreateSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "name",
            "text",
        )


class TicketListRetrieveSerializer(ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)
    messages_to_ticket = UserMessageDetailSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ("id", "name", "text", "status", "created_by", "created_at", "messages_to_ticket")


class TicketUpdateSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "id",
            "status",
        )
