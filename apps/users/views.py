from django.contrib.auth.base_user import BaseUserManager
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken, VerifyJSONWebToken
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import update_last_login
from .serializers import CreateUserSerializer, UserSerializer

from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth import get_user_model

# Login de usuário


class Login(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        return result


class CreateUserApiView(CreateModelMixin, GenericAPIView):
    """
    Cria um novo usuário
    """
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ConfirmUserApiView(GenericAPIView, BaseUserManager):
    """
    Confirma o login do usuário
    """
    permission_classes = (IsAdminUser,)
    

    def post(self, request, *args, **kwargs):
        queryset = get_object_or_404(
            get_user_model(), id=request.data.get('id', None))


        if queryset:
            users = get_user_model().objects.filter(id=request.data.get('id'),is_confirm=False)
            if users.count() :
                users.update(is_confirm=True)
                return Response(data={'mensagem': 'sucesso'}, status=200)
            else:
                return Response(data={'mensagem': 'usuário já ativado'}, status=400)
            
            
        else:
            return Response(data={'mensagem': 'Falha ao achar o usuário'}, status=404)

class UserToConfirmListApiView(ListAPIView):
    """
    Lista de usuários aguardando ativação
    """
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_queryset(self):
        users = get_user_model().objects.filter(is_confirm=False)
        return users

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class RefreshToken(VerifyJSONWebToken):
    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)

        try:
            # Atualiza o ultimo login do usuário, pois o django não atualiza logins feito por apis
            user = get_user_model().objects.get(pk=result.data['user']['id'])
            # Atualiza o ultimo login do usuário
            update_last_login(None, user)
        except Exception as e:
            pass

        return result
    