from django.contrib import admin

from tickets.models import Ticket


@admin.register(Ticket)
class Ticket(admin.ModelAdmin):
    pass
