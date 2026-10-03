from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.role == "Admin"
        )
        
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        return (
            request.user.is_authenticated
            and request.user.role == "Admin"
        )
        
class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(
        self,
        request,
        view,
        obj
    ):

        if (
            request.user.is_authenticated
            and request.user.role == "Admin"
        ):
            return True
        return obj.user == request.user