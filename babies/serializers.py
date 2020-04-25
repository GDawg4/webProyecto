from rest_framework import serializers

from babies.models import Baby


class BabySerializer(serializers.ModelSerializer):
    events = serializers.StringRelatedField(many=True)

    class Meta:
        model = Baby
        fields = (
            'id',
            'name',
            'parent',
            'events'
        )