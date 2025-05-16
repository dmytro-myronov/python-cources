from rest_framework.permissions import BasePermission, SAFE_METHODS

class PostRequiresAuthPermission(BasePermission):
    """
    Разрешает все безопасные методы (GET, HEAD, OPTIONS) без авторизации,
    но требует авторизацию для небезопасных (POST, PUT, DELETE и т.д.).
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # GET, HEAD, OPTIONS — разрешены всем
        return request.user and request.user.is_authenticated  # Остальные требуют аутентификацию
