from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _

from apps.teams.models import Team


class Robot(models.Model):

    ENERGY_BAR_COLOR_OPTIONS = (
        ('blue', _('Azul')),
        ('green', _('Verde')),
        ('yellow', _('Amarelo'))
    )

    CLASS_ROBOT_OPTIONS = (
        ('attacker', _('Attacker')),
        ('defender', _('Defender')),
        ('tricker', _('Tricker')),
        ('mechanical', _('Mechanical')),
    )

    COLOR_ROBOT_OPTIONS = (
        ('black', _('Black')),
        ('blue', _('Blue')),
        ('red', _('Red'))
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    energy = models.FloatField(_('Energia'), default=5.0)
    created_at = models.DateTimeField(_('Data da criação'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Data da última mudança'), null=True)
    color_energy = models.CharField(_('Cor da Barra de Energia'), blank=False,
                                    null=False, choices=ENERGY_BAR_COLOR_OPTIONS, max_length=16)
    class_robot = models.CharField(_('Classe'), blank=False,
                                   null=False, choices=CLASS_ROBOT_OPTIONS, max_length=16)
    color_robot = models.CharField(_('Cor do robô'), blank=False,
                                   null=False, choices=COLOR_ROBOT_OPTIONS, max_length=16)
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
