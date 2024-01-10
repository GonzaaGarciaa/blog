from rest_framework.permissions import BasePermission
from comments.models import Comment


class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_comment = view.kwargs['pk']                # Obtenemos el id del comentario
            comment = Comment.objects.get(pk=id_comment)  # Hacemos una peticon a la DB para obtener los datos del comentario
            
            id_user = request.user.pk                     # Obtenemos el id del usuario que hace la peticion
            id_user_comment = comment.user_id             # Obtenemos el id del propietario del comentario
            
            if id_user == id_user_comment:
                 return True
             
            return False