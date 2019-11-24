from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length=50,
		help_text='ej. Juan')
	correo = models.CharField(max_length=50,
		help_text='ej. juanperez@gmail.com')
	fono = models.CharField(max_length=50,
		help_text='ej. 998765432')
	motivo = models.CharField(max_length=50,
		help_text='Solo una frase')
	comentario = models.CharField(max_length=500)    
	               

	def __str__(self):
		return self.nombre	

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	class Meta:
		permissions = (
			('admin',_('es admin')),
			('usuario',_('es usuario')),
		)