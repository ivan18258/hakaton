from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Follower(models.Model):
    name = models.CharField(
        verbose_name="Имя подписчика", max_length=64)
    telegram_id = models.IntegerField(
        verbose_name="Telegram ID",
        primary_key=True)

    class Meta:
        ordering = ("telegram_id",)


class Event(models.Model):
    title = models.CharField(
        verbose_name="Название события", max_length=64)
    description = models.TextField(
        verbose_name="Описание события", max_length=512)
    time = models.DateTimeField(
        verbose_name="Время события")
    hours_to_event = models.IntegerField(
        verbose_name="Кол-во часов до события")
    owner = models.ForeignKey(
        User, verbose_name="Создатель события",
        on_delete=models.CASCADE, related_name='owner'
        )
    follower = models.ManyToManyField(Follower, through="EventFollower", blank=True)

    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("time",)


class EventFollower(models.Model):
    id_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    id_follower = models.ForeignKey(Follower, on_delete=models.CASCADE)
