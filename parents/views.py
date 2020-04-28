from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from babies.models import Baby
from babies.serializers import BabySerializer

from parents.models import Parent
from parents.serializers import ParentSerializer

from django.contrib.auth.models import User

# Create your views here.


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    baby_serializer = BabySerializer

    def perform_create(self, serializer):
        parent = serializer.save()
        user = self.request.user
        return Response(serializer.data)

    @action(detail=True, url_path='babies', methods=['get'])
    def babies(self, request, pk=None):
        allBabies = Baby.objects.all().filter(parent=pk)
        serialized = BabySerializer(allBabies, many=True)
        return Response(serialized.data)