from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from babies.models import Baby
from babies.serializers import BabySerializer

# Create your views here.


class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        return Response(serializer.data)

