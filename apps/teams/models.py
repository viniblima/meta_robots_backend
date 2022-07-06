import uuid
from django.db import models

# Create your models here.


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, max_length=16)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    members = models.ManyToManyField('robots.Robot', related_name='team')
