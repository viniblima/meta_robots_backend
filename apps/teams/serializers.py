from rest_framework import serializers
from .models import Team


class CreateTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name',)
        read_only = ('id', 'created_at', 'modifed_at', 'owner',)

    def create(self, validated_data):
        team = Team.objects.create(
            owner=self.context['request'].user,
            name=validated_data['name']
        )

        return CreateTeamSerializer(team).data


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only = ('id', 'created_at', 'modifed_at', 'owner', 'members')
