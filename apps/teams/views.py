from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin
from meta_soccer_backend.permissions import HasAccessOrDeny
from apps.teams.serializers import CreateTeamSerializer, TeamSerializer
from .models import Team
from rest_framework.response import Response


class ListTeamView(ListAPIView):
    """
    Pega todos os times disponíveis para pedir para entrar
    """

    serializer_class = TeamSerializer
    permission_classes = (HasAccessOrDeny,)

    def get_queryset(self):
        teams = Team.objects.all()
        return teams

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TeamView(CreateModelMixin, GenericAPIView):
    """
    Criar time
    """

    serializer_class = CreateTeamSerializer
    permission_classes = (HasAccessOrDeny,)

    def post(self, request, *args, **kwargs):
        queryset = Team.objects.filter(owner=request.user.id)

        if queryset.count() > 0:
            return Response(
                data={
                    'msg': 'Usuário já possui um time'
                },
                status=400
            )

        else:
            return self.create(request, *args, **kwargs)
