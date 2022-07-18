from rest_framework import serializers
from .models import RequestJoinTeam


class RequestJoinTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestJoinTeam
        fields = '__all__'
