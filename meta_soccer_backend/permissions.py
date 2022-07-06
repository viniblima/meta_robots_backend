from rest_framework import permissions


class HasAccessOrDeny(permissions.BasePermission):
    """
    Permissão customizada
    """
    message = {"errors": ["Você não tem permissão para executar essa ação."]}

    def has_permission(self, request, view):
        self.message['errors'].clear()
        self.message = {
            'message': 'Usuário não autenticado ou conta bloqueada'}
        return bool(
            request.user and request.user.is_authenticated and request.user.is_active)
