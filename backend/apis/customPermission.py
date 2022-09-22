from rest_framework.permissions import BasePermission
from .models import CustomUser

# custom permission as only whose Usertype is 1 i.e. admin are allowed on 'admin' endpoint
class isAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.UserType == "1")
