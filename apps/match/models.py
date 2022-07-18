from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from apps.teams.models import Team

# Create your models here.


class Match(models.Model):
    STATUS_OPTIONS = (
        ('scheduled', _('Scheduled')),
        ('finished', _('Finished'))
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name='first_team')
    second_team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name='second_team')
    winner = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name='winner', blank=True)
    schedule = models.DateTimeField(null=True)
    created_at = models.DateTimeField(_('Data da criação'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Data da última mudança'), null=True)

    class Meta:
        verbose_name = _('Partida')
        verbose_name_plural = _('Partidas')

    def __str__(self):
        return str('{0} - {1}'.format(self.first_team.name, self.second_team.name))
