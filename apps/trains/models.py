from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _

from apps.robots.models import Robot
from django.conf import settings


class Train(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    trained_attribute = models.CharField(
        _('Atributo treinado'), blank=False, null=False, choices=settings.ATTRIBUTES, max_length=16)
    created_at = models.DateTimeField(_('Data da criação'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Data da última mudança'), null=True)

    class Meta:
        verbose_name = _('Treino')
        verbose_name_plural = _('Treinos')

    def __str__(self):
        return str('{0} - {1}'.format(self.robot.id, self.trained_attribute))
