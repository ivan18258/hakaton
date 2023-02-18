# Generated by Django 4.1.7 on 2023-02-18 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('name', models.CharField(max_length=64, verbose_name='Имя подписчика')),
                ('telegram_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Telegram ID')),
            ],
            options={
                'ordering': ('telegram_id',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название события')),
                ('description', models.TextField(max_length=512, verbose_name='Описание события')),
                ('time', models.DateTimeField(verbose_name='Время события')),
                ('hours_to_event', models.IntegerField(verbose_name='Кол-во часов до события')),
                ('follower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='follower', to='event.follower', verbose_name='Подписчик события')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Создатель события')),
            ],
            options={
                'ordering': ('time',),
            },
        ),
    ]
