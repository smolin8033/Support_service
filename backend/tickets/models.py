from django.db import models

from tickets.constants import STATUS_CHOICES
from users.models import User


class Ticket(models.Model):
    """Тикеты"""

    name = models.CharField(max_length=60)
    text = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="U")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
