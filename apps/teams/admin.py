from django.contrib import admin

from apps.teams.forms import TeamForm

from .models import Team

# Register your models here.


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    form = TeamForm
    readonly_fields = ('created_at', 'modified_at',)
