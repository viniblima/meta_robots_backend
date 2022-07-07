import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, max_length=16)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    members = models.ManyToManyField(
        'robots.Robot', related_name='members', blank=True)
    created_at = models.DateTimeField(_('Data da criação'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Data da última mudança'), null=True)

    class Meta:
        verbose_name = _('Time')
        verbose_name_plural = _('Times')

    def __str__(self):
        return str('{0} - {1}'.format(self.name, self.owner.name))
