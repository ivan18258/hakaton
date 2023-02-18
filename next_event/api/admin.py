from django.contrib import admin
from event.models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Событие"""
    fields = (
        'title',
        'description',
        'time',
        'reminder_to_event_1',
        'reminder_to_event_1',
        'follower',
    )

    list_display = (
        'title',
        'description',
        'time',
        'reminder_to_event_1',
        'reminder_to_event_1',
        'follower',
    )
