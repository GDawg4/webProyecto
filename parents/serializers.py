from rest_framework import serializers

from parents.models import Parent
from babies.models import Baby
from django.contrib.auth.models import User

class ParentSerializer(serializers.ModelSerializer):
    babies = serializers.PrimaryKeyRelatedField(many=True, queryset=Baby.objects.all())
    class Meta:
        model = Parent
        fields = (
            'id',
            'name',
            'babies'
        )


