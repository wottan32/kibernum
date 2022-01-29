from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import permissions


class TodoListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # buscar datos con id
    def get_object(self, id):
        try:
            return Usuario.objects.get(id=id)
        except Usuario.DoesNotExist:
            return None

    # Rescatar todos los usuarios
    def get(self, request, *args, **kwargs):
        todo_instance = self.get_object(request.user.id)
        if not todo_instance:
            return Response(
                {"res": "El objeto con id no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UsuarioSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Actualizar usuarios
    def put(self, request, *args, **kwargs):
        todo_instance = self.get_object(request.user.id)
        if not todo_instance:
            return Response(
                {"res": "el objeto con el id no se encuentra"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'id': request.data.get('id'),
            'nombre': request.data.get('nombre'),
            'apellido': request.data.get('apellido'),
            'email': request.data.get('email'),
            'fechaNac': request.data.get('fechaNac'),
        }
        serializer = UsuarioSerializer(instance=todo_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Borrar usuario
    def delete(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with app id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


'''
    # Crear usuario
    def post(self, request, *args, **kwargs):
        data = {
            'id': request.data.get('id'),
            'nombre': request.data.get('nombre'),
            'apellido': request.data.get('apellido'),
            'email': request.data.get('email'),
            'fechaNac': request.data.get('fechaNac'),
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''


class TodoDetailApiView:
    pass
