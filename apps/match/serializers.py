from rest_framework import serializers
from .models import Match
from datetime import datetime
from apps.teams.models import Team


class CreateMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

    def create(self, validated_data):
        for team in Team.objects.all():
            print(team)
            have_match = Match.objects.filter(
                first_team=team) | Match.objects.filter(second_team=team)

            if have_match.count():
                print('have_match')
            else:
                opponents = Team.objects.exclude(id=team.id)

                for opponent in opponents:
                    opponent_have_match = Match.objects.filter(
                        first_team=opponent) | Match.objects.filter(second_team=opponent)

                    if opponent_have_match.count():
                        print('opponent_have_match')
                        break
                    else:
                        new_match = Match.objects.create(
                            first_team=team,
                            second_team=opponent,
                            schedule=datetime.now()
                        )
                        print(new_match)
                        new_match.save()
                        break
            return validated_data
