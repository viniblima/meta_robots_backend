from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from apps.robots.models import Robot

from apps.trains.serializers import TrainSerializer
from meta_soccer_backend.permissions import HasAccessOrDeny
from rest_framework.response import Response
from django.conf import settings

# Create your views here.


class TrainRobot(CreateModelMixin, GenericAPIView):
    """
    Treinar robô
    """

    serializer_class = TrainSerializer
    permission_classes = (HasAccessOrDeny,)

    def post(self, request, *args, **kwargs):
        robot_query = Robot.objects.filter(
            id=request.data['robot'])

        if robot_query.count() < 1:
            return Response(data={'mensagem': 'Robô não encontrado'}, status=404)

        if robot_query.first().energy < 1.0:
            return Response(data={'mensagem': 'Robô sem energia'}, status=400)

        if request.data['trained_attribute'] in settings.TRAIN_OBJ:

            return self.create(request, *args, **kwargs)
        else:
            return Response(data={'mensagem': 'Atributo inexistente'}, status=404)
