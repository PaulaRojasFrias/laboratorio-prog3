from django.db import models

# Create your models here.

class Administrador(models.Model):

     class Meta:
        permissions = [
            ("permiso_administrador", "Permiso administrador"),
        ]
