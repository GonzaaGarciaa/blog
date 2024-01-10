from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from users.models import User

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True): # Si es valido pasa, sino salta una excepcion
            serializer.save() # Guardamos el usuario
            return Response(serializer.data) # Mandamos los datos del usuario
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Mandamos los datos y generamos un error por si no entro correctamente
    
class UserView(APIView):
    permission_classes = [IsAuthenticated] # De esta manera solo los usuarios autenticados podran hacer esta peticion
    
    # Hacemos un override del metodo get
    def get(self, request):
        serializer = UserSerializer(request.user) # En request.user tenemos todos lo datos de usuario
        return Response(serializer.data)
    
    # Hacemos un override del metodo put
    def put(self, request):
        user = User.objects.get(id=request.user.id) # De esta manera obtenemos el id del usuario del request
        serializer = UserUpdateSerializer (user, request.data) # Le pasamos los datos actuales del usuario y los nuevos datos del usuario (last_name y first_name)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)