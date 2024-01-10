from django.db import models
from django.db.models import CASCADE
from users.models import User
from posts.models import Post

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # Cuando se registre un nuevo comentario automaticamente se le ponga la fecha de creacion
    user = models.ForeignKey(User, on_delete=CASCADE, null=True) # cuando borremos el usuario se borran todos los comentarios, el null=True es por si queremos tener la posibilidad de sacar el comentario de algun usuario
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True) # Si eliminamos el post se eliminan los comentarios, con el null=true tenemos la posibilidad de dejar algun comentario sin post por si nos interesa
    
    
    
