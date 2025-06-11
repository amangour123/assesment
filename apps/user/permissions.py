from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.name == 'admin'

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.name == 'manager'

class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.name in ['admin', 'manager']
    
class IsAssigneeOrAdminManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.assigned_to == request.user or
            (request.user.role and request.user.role.name in ['admin', 'manager'])
        )
