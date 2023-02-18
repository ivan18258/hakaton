from django.contrib import admin
from event.models import Event, Follower

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Событие"""
    fields = (
        'title',
        'description',
        'time',
        'hours_to_event',
        'follower',
        'owner',
    )

    list_display = (
        'title',
        'description',
        'time',
        'follower',
        'hours_to_event',
        'owner',
    )
    
@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'telegram_id',
    )

    list_display = (
        'name',
        'telegram_id',
    )