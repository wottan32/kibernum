import uuid
from rest_framework import serializers

# from django.contrib.auth.models import Usuario
from app.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()

    class Meta:
        model = Usuario
        fields = '__all__'


class ProbarSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=200)
    apellido = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    fechaNac = serializers.DateTimeField()

    def validate_email(self, value):
        lower_email = value.lower()
        if Usuario.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Duplicate")
        return lower_email

    def validate(self, data):
        print("Validado")
        return data
