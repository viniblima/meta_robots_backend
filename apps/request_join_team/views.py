from datetime import datetime
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin

from apps.teams.models import Team
from .models import RequestJoinTeam
from meta_soccer_backend.permissions import HasAccessOrDeny
from .serializers import RequestJoinTeamSerializer
from rest_framework.response import Response
from apps.robots.models import Robot
from django.shortcuts import get_object_or_404


class AuthorizeJoinTeam(GenericAPIView):
    permission_classes = (HasAccessOrDeny,)

    def post(self, request):
        team = Team.objects.get(owner=self.request.user.id)

        requests = RequestJoinTeam.objects.filter(
            id=request.data.get('id'), team=team.id).values()

        if requests.count():

            if requests.values().first()['status'] != 'requested':
                return Response(
                    data={
                        'mensagem': 'Request já finalizada'
                    },
                    status=401
                )
            else:
                requests.update(status='accepted', modified_at=datetime.now())
                return Response(
                    data=requests.values().first()
                )
        else:
            return Response(
                data={
                    'mensagem': 'Request com esse id não encontrado ou time não pertence à esse usuário'
                },
                status=404
            )


class RequestJoinTeamView(CreateModelMixin, GenericAPIView):
    """
    Pedir para entrar em time
    """

    serializer_class = RequestJoinTeamSerializer
    permission_classes = (HasAccessOrDeny,)

    def post(self, request, *args, **kwargs):
        queryset = RequestJoinTeam.objects.filter(
            robot=request.data['robot'], status='requested',
        )

        robot = Robot.objects.filter(
            user=request.user.id, id=request.data['robot'])

        if robot.count() < 1:
            return Response(data={'mensagem': 'Robô não pertence a esse usuário', }, status=401)

        if queryset.count() > 0:
            return Response(data={'mensagem': 'Já existe um pedido para esse robô', }, status=400)

        else:
            return self.create(request, *args, **kwargs)

    def get(self, request):
        team = get_object_or_404(Team, owner=request.user.id)

        queryset = RequestJoinTeam.objects.filter(
            team=team.id, status='requested').values()

        return Response(
            data=queryset,
            status=200
        )
