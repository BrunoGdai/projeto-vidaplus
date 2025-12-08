from rest_framework.permissions import BasePermission
from .models import PerfilPermissao

class HasPermission(BasePermission):
    def has_permission(self, request, view):
        usuario = request.user
        if usuario is None:
            return False

        required_permission = getattr(view, "required_permission", None)
        if required_permission is None:
            return True

        return PerfilPermissao.objects.filter(
            perfil_id=usuario.perfil_id, permissao_id=required_permission
        ).exists()
