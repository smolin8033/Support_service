from django.contrib import admin

from user_messages.models import UserMessage


@admin.register(UserMessage)
class UserMessage(admin.ModelAdmin):
    pass
