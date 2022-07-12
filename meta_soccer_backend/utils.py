from datetime import timedelta
from django.utils import timezone
from rest_framework.permissions import BasePermission
from apps.robots.models import Robot
from apps.users.serializers import UserSerializer
from django.conf import settings


def jwt_response_payload_handler(token, user=None, request=None):
    robots = []

    for element in UserSerializer(user).data['robots']:
        robots.append(Robot.objects.filter(id=element).values().first())

    return {
        'token': token,
        'expires_in': timezone.now() + timedelta(hours=settings.TOKEN_EXPIRED_AFTER_HOURS),
        'user': {
            'id': UserSerializer(user, context={'request': request}).data['id'],
            'date_of_birth': UserSerializer(user, context={'request': request}).data['date_of_birth'],
            'name': UserSerializer(user, context={'request': request}).data['name'],
            'email': UserSerializer(user, context={'request': request}).data['email'],
            'gender': UserSerializer(user, context={'request': request}).data['gender'],
            'is_staff': UserSerializer(user, context={'request': request}).data['is_staff'],
            'is_confirm': UserSerializer(user, context={'request': request}).data['is_confirm'],
        },
        'robots': robots
    }


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff
