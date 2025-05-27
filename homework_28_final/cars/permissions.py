from rest_framework.permissions import BasePermission, SAFE_METHODS

class PostRequiresAuthPermission(BasePermission):
    """
    Allow only save methods
    """

    def has_permission(self, request, view) ->bool:
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
