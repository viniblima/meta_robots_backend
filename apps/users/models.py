from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models

import uuid
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    @classmethod
    def normalize_email(cls, email):
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = email_name + '@' + domain_part
        return email.lower()

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_('Preencha com um email válido'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.username = email
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        print('created')
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_confirm', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_confirm', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if not password:
            raise ValueError("User must have a password")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    username = None
    first_name = None
    last_name = None

    # Opções de gênero
    GENDER_OPTIONS = (
        ('Mulher', _('Mulher')),
        ('Homem', _('Homem')),
        ('Outro', _('Não me identifico'))
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_of_birth = models.DateField(
        _('Data de nascimento'), blank=True, null=True)

    name = models.CharField(_('Nome / Apelido'),
                            max_length=256, blank=False, null=False, )
    email = models.EmailField(_('email'), max_length=256, unique=True,
                              error_messages={
                                  'unique': _("Já existe um usuario cadastrado com este email."),
    }, )
    gender = models.CharField(_('Gênero'), blank=False,
                              null=False, choices=GENDER_OPTIONS, max_length=16)
    created_at = models.DateTimeField(_('Data de criação'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Data de atualização'), auto_now=True)
    is_staff = models.BooleanField(
        _('Staff status'),
        default=False,
        help_text=_('Define se esse usuário pode logar no site admin')
    )
    robots = models.ManyToManyField(
        'robots.Robot', related_name='robots', blank=True)
    is_active = models.BooleanField(_('Ativo'), default=True)
    is_confirm = models.BooleanField(_('Ativo'), default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]

    def save(self, *args, **kwargs):
        self.email = self.email.lower()

        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save(update_fields=['is_active'])

    def clean(self, *args, **kwargs):
        if self.robots.count() > 3:
            raise ValidationError('Nao pode ter mais de 3 robos por usuário')
        return super(User, self).clean(*args, **kwargs)

    class Meta:
        # abstract = False
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def save(self, *args, **kwargs):
        self.email = self.email.lower()

        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save(update_fields=['is_active'])
