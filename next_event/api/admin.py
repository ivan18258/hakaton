from django.contrib import admin
from event.models import Event, Follower, EventFollower

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Событие"""
    fields = (
        'title',
        'description',
        'time',
        'hours_to_event',
        'owner',
    )

    list_display = (
        'title',
        'description',
        'time',
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


@admin.register(EventFollower)
class EventFollower(admin.ModelAdmin):
    fields = (
        'id_event',
        'id_follower',
    )

    list_display = (
        'id_event',
        'id_follower',
    )