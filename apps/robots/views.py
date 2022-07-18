from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from apps.request_join_team.models import RequestJoinTeam
from apps.robots.models import Robot

from meta_soccer_backend.permissions import HasAccessOrDeny
from .serializers import RobotSerializer
import uuid

# Create your views here.


class CreateRobot(CreateModelMixin, GenericAPIView):
    """
    Criar robô
    """
    serializer_class = RobotSerializer
    permission_classes = (HasAccessOrDeny,)

    def get(self, request):
        queryset = Robot.objects.filter(
            id=request.data.get('id'))

        if queryset.count():
            if queryset.values().first()['user_id'] == request.user.id:
                queryset.values().first()['request'] = RequestJoinTeam.objects.filter(
                    robot=request.data.get('id'), status='requested').values().first()

            return Response(
                data=queryset
            )
        else:
            return Response(
                data={'mensagem': 'Robô não encontrado'},
                status=404
            )

    def post(self, request, *args, **kwargs):
        id = str('{0}'.format(request.user.id))

        robots = Robot.objects.filter(user=id)
        if robots.count() >= 3:
            return Response(
                data={
                    'msg': 'Limite de robôs atingido'
                },
                status=400
            )
        return self.create(request, *args, **kwargs)
