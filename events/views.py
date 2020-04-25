from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from events.models import Event
from events.serializers import EventSerializer

# Create your views here.


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        parent = serializer.save()
        user = self.request.user
        return Response(serializer.data)