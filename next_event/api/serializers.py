from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from event.models import Event, Follower


class FollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follower
        fields = ('id', 'name', 'telegram_id')

class EventSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        fields = '__all__'
        model = Event

class EventMiniSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'time', 'hours_to_event')
        model = Event

