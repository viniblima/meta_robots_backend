from django.contrib import admin
from .forms import RequestJoinTeamForm
from .models import RequestJoinTeam

# Register your models here.


@admin.register(RequestJoinTeam)
class RequestJoinTeamAdmin(admin.ModelAdmin):
    form = RequestJoinTeamForm
    readonly_fields = ('created_at', 'modified_at',)
