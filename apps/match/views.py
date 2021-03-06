from rest_framework.generics import GenericAPIView
from apps.match.models import Match
from apps.teams.models import Team
from meta_soccer_backend.permissions import HasAccessOrDeny
from datetime import datetime
from rest_framework.response import Response


class CreateMatch(GenericAPIView):
    permission_classes = (HasAccessOrDeny,)

    async def post(self, request):
        for team in Team.objects.all():
            print(team)
            have_match = Match.objects.filter(
                first_team=team) | Match.objects.filter(second_team=team)

            if have_match.count():
                print(have_match)
            else:
                opponents = Team.objects.exclude(id=team.id)

                for opponent in opponents:
                    opponent_have_match = Match.objects.filter(
                        first_team=opponent) | Match.objects.filter(second_team=opponent)

                    if opponent_have_match.count():
                        print('opponent_have_match')
                        break
                    else:
                        new_match = await Match.objects.create(
                            first_team=team,
                            second_team=opponent,
                            schedule=datetime.now()
                        )
                        break
        return Response(
            data=Match.objects.all().values()
        )
