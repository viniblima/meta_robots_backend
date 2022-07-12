from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from apps.robots.models import Robot

from meta_soccer_backend.permissions import HasAccessOrDeny
from .serializers import RobotSerializer

# Create your views here.


class CreateRobot(CreateModelMixin, GenericAPIView, UpdateModelMixin):
    """
    Criar robô
    """
    serializer_class = RobotSerializer
    permission_classes = (HasAccessOrDeny,)

    def post(self, request, *args, **kwargs):
        id = str('{0}'.format(request.user.id))
        if id != request.data['user']:
            return Response(
                data={
                    'msg': 'Usuário diferente do logado'
                },
                status=400
            )
        robots = Robot.objects.filter(user=id)
        if robots.count() >= 3:
            return Response(
                data={
                    'msg': 'Limite de robôs atingido'
                },
                status=400
            )
        return self.create(request, *args, **kwargs)
