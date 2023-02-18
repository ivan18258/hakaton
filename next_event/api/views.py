from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from event.models import Event

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all