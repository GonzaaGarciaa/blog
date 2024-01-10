from rest_framework.permissions import BasePermission

class IsAdmindOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff
        
# Simplemente estamos diciendo que si la peticion es 'GET' todos pueden pasar, de lo contrario tiene que ser staff