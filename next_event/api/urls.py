from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (EventViewSet, EventMiniViewSet)

app_name = 'api'

routerV1 = DefaultRouter()
routerV1.register(r'events', EventViewSet, basename='titles')
routerV1.register(r'events_mini', EventMiniViewSet, basename='titles')
urlpatterns = [
    path('v1/', include(routerV1.urls)),
]