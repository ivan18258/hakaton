from django.contrib import admin
from event.models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Событие"""
    fields = (
        'title',
        'description',
        'time',
        'hours_to_event',
        'follower',
    )

    list_display = (
        'title',
        'description',
        'time',
        'follower',
        'hours_to_event',
    )
    
