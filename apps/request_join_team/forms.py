from django import forms

from .models import RequestJoinTeam


class RequestJoinTeamForm(forms.ModelForm):
    class Meta:
        model = RequestJoinTeam
        fields = '__all__'
