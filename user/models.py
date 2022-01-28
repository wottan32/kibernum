import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Usuario(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nombre = models.TextField(blank=False)
    apellido = models.TextField(blank=False)
    email = models.EmailField(blank=False)
    fecha = models.DateTimeField(blank=False)

    def __str__(self):
        return self.id
