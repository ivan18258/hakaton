from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from event.models import Event, Follower


class FollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follower

        fields = ('name', 'telegram_id',)



class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'title',  'description', 'time', 'image')
        

    def create(self, validated_data):
        followers = validated_data.pop('follower')
  
        event = Event.objects.create(**validated_data)

        for follower in followers:
            # Создадим новую запись или получим существующий экземпляр из БД
            current_follower, status = Follower.objects.get_or_create(
                **follower)
            Follower.objects.create(
                follower=current_follower, event=event)
        return event

class EventMiniSerializer(serializers.ModelSerializer):
    follower = FollowerSerializer(many=True, required=False,)
    class Meta:
        fields = ('id', 'time', 'hours_to_event', 'follower')
        model = Event

    def create(self, validated_data):
        followers = validated_data.pop('follower')
  
        event = Event.objects.create(**validated_data)

        for follower in followers:
            # Создадим новую запись или получим существующий экземпляр из БД
            current_follower, status = Follower.objects.get_or_create(
                **follower)
            Follower.objects.create(
                follower=current_follower, event=event)
        return event

