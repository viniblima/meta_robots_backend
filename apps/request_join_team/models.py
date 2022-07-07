from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _

from apps.robots.models import Robot
from apps.teams.models import Team

# Create your models here.


class RequestJoinTeam(models.Model):
    STATUS_OPTIONS = (
        ('requested', _('Requested')),
        ('accepted', _('Accepted')),
        ('rejected', _('Rejected')),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    status = models.CharField(_('Status'), blank=False,
                              null=False, default='requested', choices=STATUS_OPTIONS, max_length=16)
    created_at = models.DateTimeField(_('Data da criação'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Data da última mudança'), null=True)

    class Meta:
        verbose_name = _('Pedido para entrar em time')
        verbose_name_plural = _('Pedidos para entrar em time')

    def __str__(self):
        return str('{0} - {1}'.format(self.robot.id, self.team.name))
