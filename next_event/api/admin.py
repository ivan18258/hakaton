from django.contrib import admin
from event.models import Event, Follower, EventFollower
from django.utils.safestring import mark_safe
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Событие"""
    fields = (
        'title',
        'description',
        'time',
        'hours_to_event',
        'owner',
        'image',
        "preview"
    )
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')

    list_display = (
        'title',
        'description',
        'time',
        'hours_to_event',
        'owner',
        'image',
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