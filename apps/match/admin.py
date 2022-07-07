from django.contrib import admin
from apps.match.forms import MatchForm
from apps.match.models import Match

# Register your models here.


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    form = MatchForm
    readonly_fields = ('created_at', 'modified_at')
