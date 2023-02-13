from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from users.constants import ROLE_CHOICES


# Create your models here.
class User(AbstractUser):
    """
    Пользователь. Может быть либо из службы поддержки, либо пользователем
    """

    role = models.CharField(max_length=30, blank=True, choices=ROLE_CHOICES)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password"]

    objects = UserManager()
