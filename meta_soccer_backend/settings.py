"""
Django settings for meta_soccer_backend project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import datetime

import dj_database_url

from django.utils.translation import ugettext_lazy as _

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cs8^1vq!6#($@k8gji5ioswo#(zhb+#)-$e2d1d^7x_odvqw@_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    # apps
    'apps.users',
    'apps.teams',
    'apps.robots',
    'apps.request_join_team',
    'apps.match',
    'apps.trains'
]

# REST Configuration
REST_FRAMEWORK = {
    'DATETIME_FORMAT': '%d/%m/%YT%H:%M:%S%z',
    'DATETIME_INPUT_FORMATS': ['%d/%m/%YT%H:%M:%S%z'],
    'DATE_INPUT_FORMATS': ['%d/%m/%Y'],
    'DATE_FORMAT': '%d/%m/%Y',
    'DEFAULT_PERMISSION_CLASSES': (
        'meta_soccer_backend.permissions.HasAccessOrDeny',
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

TOKEN_EXPIRED_AFTER_HOURS = 24

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

ATTRIBUTES = (
    ('strength', _('STRENGTH')),
    ('speed', _('SPEED')),
    ('skill', _('SKILL')),
    ('defense', _('DEFENSE'))
)

TRAIN_OBJ = {
    'strength': 1.0,
    'speed': 1.0,
    'skill': 1.0,
    'defense': 1.0
}

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'meta_soccer_backend.utils.jwt_response_payload_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=TOKEN_EXPIRED_AFTER_HOURS),
    'JWT_ALLOW_REFRESH': True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meta_soccer_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'meta_soccer_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=config(
            'DATABASE_URL', default="postgis://root:example@db:5432/database"),
    )
}
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'
DATABASES['default']['TEST'] = {
    'NAME': 'test_db'
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'users.User'


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False

DEFENDER_USERNAME_FORM_FIELD = 'email'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
