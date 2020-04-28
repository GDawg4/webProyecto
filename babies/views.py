from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from babies.models import Baby
from events.models import Event
from babies.serializers import BabySerializer
from events.serializers import EventSerializer
from guardian.shortcuts import assign_perm
from permissions.services import APIPermissionClassFactory
# Create your views here.


def is_parent(user, obj, request):
    return user.username == obj.parent.name


class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': is_parent,
                    'list': False,
                },
                'instance': {
                    'retrieve': is_parent,
                    'destroy': is_parent,
                    'update': is_parent,
                    'partial_update': is_parent,
                    'events': is_parent,
                    # 'update_permissions': 'users.add_permissions'
                    # 'archive_all_students': phase_user_belongs_to_school,
                    # 'add_clients': True,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('babies.change_baby', user, baby)
        assign_perm('babies.view_baby', user, baby)
        return Response(serializer.data)

    @action(detail=True, url_path='events', methods=['get'])
    def events(self, request, pk=None):
        allEvents = Event.objects.all().filter(baby=pk)
        serialized = EventSerializer(allEvents, many=True)
        return Response(serialized.data)

