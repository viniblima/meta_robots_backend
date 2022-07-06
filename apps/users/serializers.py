from rest_framework import serializers
from .models import User

import django.contrib.auth.password_validation as validators

from django.core import exceptions
from rest_framework_jwt.settings import api_settings

from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'date_of_birth', 'name', 'email', 'gender', 'is_staff', 'is_confirm'
        )

        read_only = (
            'created_at', 'updated_at', 'is_staff'
        )


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('password_confirm', 'password',
                  'email', 'gender', 'name')

        # fields = ('__all__')
        read_only = ('id', 'is_staff')

    def to_representation(self, instance):
        return instance

    def validate(self, attrs):

        user = User(attrs['name'], attrs['email'])

        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')

        if not password or not password_confirm:
            raise serializers.ValidationError('Senhas requeridas')

        if password != password_confirm:
            raise serializers.ValidationError('Senhas não conferem')

        errors = dict()
        try:
            validators.validate_password(password=password, user=user)

        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        # Remove a confirmação de senha pois não é necessária para gravar um usuário
        del attrs['password_confirm']
        # del attrs['username']
        return super(CreateUserSerializer, self).validate(attrs)

    def create(self, validated_data):
        # with transaction.atomic():
        user = User(
            email=validated_data['email'],
            gender=validated_data['gender'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        try:
            user.full_clean(validate_unique=True)

        except Exception as e:
            print(e)

        user = User.objects.create_user(email=validated_data['email'],
                                        name=validated_data['name'],
                                        gender=validated_data['gender'],
                                        password=validated_data['password'],
                                        )
        # user.save()

        try:
            User.objects.filter(id=user.id)

        except Exception as e:
            print(e)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return {'token': token, 'data': UserSerializer(user).data}
