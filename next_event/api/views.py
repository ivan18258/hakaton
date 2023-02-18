from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from event.models import Event, Follower
from .serializers import (EventSerializer, EventMiniSerializer,)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventMiniViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventMiniSerializer
    




