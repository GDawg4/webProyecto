from rest_framework import viewsets
from rest_framework.response import Response
from guardian.shortcuts import assign_perm
from events.models import Event
from events.serializers import EventSerializer
from permissions.services import APIPermissionClassFactory


def is_of_child(user, obj, request):
    return user.first_name == obj.baby.parent.name


def test():
    return False


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (APIPermissionClassFactory(
        name='eventPermission',
        permission_configuration={
                'base': {
                    'create': test(),
                    'list': False,
                },
                'instance': {
                    'retrieve': is_of_child,
                    'destroy': is_of_child,
                    'update': is_of_child,
                    'partial_update': is_of_child,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        event = serializer.save()
        user = self.request.user
        assign_perm('events.change_event', user, event)
        assign_perm('events.view_event', user, event)
        return Response(serializer.data)

