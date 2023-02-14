from django.db import models

from tickets.models import Ticket
from users.models import User


class UserMessage(models.Model):
    """Сообщения к тикетам"""

    text = models.TextField()
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="messages_to_ticket")
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_of_user", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:100]
