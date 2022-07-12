from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from apps.teams.models import Team
from django.conf import settings


class Robot(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    energy = models.FloatField(_('Energia'), default=5.0)
    created_at = models.DateTimeField(_('Data da criação'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Data da última mudança'), null=True)
    color_energy = models.CharField(_('Cor da Barra de Energia'), blank=False,
                                    null=False, choices=settings.ENERGY_BAR_COLOR_OPTIONS, max_length=16)
    class_robot = models.CharField(_('Classe'), blank=False,
                                   null=False, choices=settings.CLASS_ROBOT_OPTIONS, max_length=16)
    color_robot = models.CharField(_('Cor do robô'), blank=False,
                                   null=False, choices=settings.COLOR_ROBOT_OPTIONS, max_length=16)
    strength = models.FloatField(_('Força'))
    speed = models.FloatField(_('Velocidade'))
    skill = models.FloatField(_('Habilidade'))
    defense = models.FloatField(_('Defesa'))
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='Time')

    class Meta:
        verbose_name = _('Robô')
        verbose_name_plural = _('Robôs')

    def __str__(self):
        return str('{0} - {1}'.format(self.user.name, self.id))
