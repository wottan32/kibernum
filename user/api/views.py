from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from user.models import Usuario
from .serializers import UsuarioSerializer

class UsuarioListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    #listar todos los usuarios
    def get(self, request, *args, **kwargs):
        user = Usuario.objects.filter(id = request.user.id)
        serializar =UsuarioSerializer(user, many=True)
        return Response(serializar.data, status=status.HTTP_200_OK)

    # Crear usuario
    def post(selfself, request, *args, **kwargs):
        data = {
            'id':request.data.get('id'),
            'completed': request.data.get('completed'),
            'user': request.user.id
        }
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

