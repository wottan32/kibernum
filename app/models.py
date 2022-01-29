import uuid
from django.db import models


class Usuario(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    fechaNac = models.DateTimeField()

    def __str__(self):
        return self.id
