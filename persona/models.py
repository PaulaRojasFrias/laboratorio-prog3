from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your models here.
class AbstractPersona(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)

    class Meta:
        abstract = "true"
        ordering = ('apellido', 'nombre')

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
 

class Docente(AbstractPersona):
    cuil = models.CharField(max_length=11, unique=True)
    correo = models.EmailField(max_length=254)
    crear_usuario = models.BooleanField(default=False) 

class Alumno(AbstractPersona):
    dni = models.CharField(max_length=8, unique=True)
    matricula = models.CharField(max_length=5, unique=True) #Pueden ser dos?
    correo = models.EmailField(max_length=254)

class Asesor(AbstractPersona):
    cuil = models.CharField(max_length=11, unique=True) #modificado
    curriculum = models.FileField(upload_to='persona/')

@receiver(post_save, sender=Docente)
def crear_usuario_docente(sender, instance, created, **kwargs):
    if created and instance.crear_usuario:
        username = instance.cuil
        password = User.objects.make_random_password()
        user = User.objects.create_user(username=username, password=password)
        user.email = instance.correo
        user.save()

        # Envía el correo electrónico con las credenciales
        send_mail(
            'Datos de usuario',
            f'Nombre de usuario: {username}\nContraseña: {password}',
            'sistemadeseguimientoPTF@gmail.com',
            [instance.correo],
            fail_silently=True,
        )

@receiver(post_save, sender=Alumno)
def crear_usuario_alumno(sender, instance, created, **kwargs):
    # No se verifica la condición crear_usuario aquí para el modelo Alumno
    if created:
        username = instance.dni
        password = User.objects.make_random_password()
        user = User.objects.create_user(username=username, password=password)
        user.email = instance.correo
        user.save()

        # Envía el correo electrónico con las credenciales
        send_mail(
            'Datos del usuario',
            f'Nombre de usuario: {username}\nContraseña: {password}',
            'sistemadeseguimientoPTF@gmail.com',  # Reemplaza con tu dirección de correo
            [instance.correo],
            fail_silently=True,
        )