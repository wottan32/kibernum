from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import Response

from app.api.serializers import UsuarioSerializer
from app.models import Usuario

usuario_serializer = UsuarioSerializer


@api_view(['GET', 'POST'])
def usuario_api_view(request):
    # listar usuario
    if request.method == 'GET':
        Usuario.objects.all()
        return Response(usuario_serializer.data, status=status.HTTP_200_OK)

    # Crear usuario
    elif request.method == 'POST':
        usuarios_serializer = UsuarioSerializer(data=request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data, status=status.HTTP_201_CREATED)
        return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail_api_view(request, pk=None):
    usuario = Usuario.objects.filter(id=pk).first()

    # Traer datos usuario
    if request.method == 'GET':
        usuario = Usuario.objects.filter(id=pk).first()
        usuario_serializer = UsuarioSerializer(usuario)
        return Response(usuario_serializer.data, status=status.HTTP_200_OK)

    # actualizacion datos usuario
    elif request.method == 'PUT':
        usuario = Usuario.objects.filter(id=pk).first()
        usuario_serializer = UsuarioSerializer(usuario, data=request.data)

        # Validacion
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data, status=status.HTTP_200_OK)
        return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar usuario
    elif request.method == 'DELETE':
        usuario = Usuario.objects.filter(id=pk).first()
        usuario.delete()
        return Response({'message': 'Usuario eliminado'}, status=status.HTTP_200_OK)
    return Response({'message': 'No se ha encontrado Usuario'}, status=status.HTTP_400_BAD_REQUEST)
