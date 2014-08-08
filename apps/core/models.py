from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


from django.utils.encoding import iri_to_uri
from django.utils.http import urlquote

class Torneo(models.Model):
	"""
	modelo para torneo
	"""
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=200)
	fecha_inicio = models.DateTimeField()
	fecha_finalizacion = models.DateTimeField()
	#creador = models.ForeignKey(Friki)
	visibilidad_problemas =  models.BooleanField(default=False)

	def __unicode__(self):
		return u"%s - %s" % (self.id, self.nombre)


class Problema(models.Model):
	"""
	Su nombre lo dice
	"""
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=200)
	dificultad = models.IntegerField()
	#torneo = models.ForeignKey(Torneo)
	torneo = models.ManyToManyField(Torneo)

	def __unicode__(self):
		return u'%s - %s' % (self.id, self.nombre)

class MyFrikiManager(BaseUserManager):
	"""
	Manejador para la clase usuario, sin esto no se pueden tener usuarios personalizados
	"""
	def _create_user(self, email, alias, password, is_staff, is_superuser, **extra_fields):
		if not email:
			raise ValueError('El email debe ingresarse')
		
		email = self.normalize_email(email)
		user = self.model( email=email, alias=alias, is_active=True, is_staff=is_staff, is_superuser=is_superuser,**extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, alias, password=None, **extra_fields):
		return self._create_user( email, alias, password,  False, False, **extra_fields)

	def create_superuser(self,  email, alias, password, **extra_fields):
		return self._create_user( email, alias, password,  True, True, **extra_fields)


class Friki(AbstractBaseUser, PermissionsMixin):
	"""
	Los usuarios son representados por este modelo
    """
	email = models.EmailField(unique=True)
	alias = models.CharField(unique=True, max_length=15)
	torneo = models.ManyToManyField(Torneo)


	is_active = models.BooleanField (default=True)
	is_staff = models.BooleanField (default=False)

	objects = MyFrikiManager()

	USERNAME_FIELD = 'email'	#campo login
	REQUIRED_FIELDS = ['alias']

	def get_short_name(self):
		return self.alias


class Estado(models.Model):
	"""
	Representa el estado en el que se encuentra un solucion enviada (En cola, Error de compilacion, etc)
	"""
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=250)

	def __unicode__(self):
		return self.nombre

class Lenguaje(models.Model):
	"""
	Representa el lnguaje de programacion
	"""
	nombre = models.CharField(max_length=10)

	def __unicode__(self):
		return self.nombre
		
class Solucion(models.Model):
	"""
	Representa las soluciones a los problemas que han sido enviadas
	"""

	def path(instance, filename):
		path = 'soluciones/%s/%s-%s/%s/' % (instance.torneo.id, instance.friki.id, instance.friki.alias, instance.problema.id)
		return path

	fecha_envio = models.DateTimeField(auto_now_add=True)	
	problema = models.ForeignKey(Problema)
	friki = models.ForeignKey(Friki)
	estado = models.ForeignKey(Estado)	
	lenguaje = models.ForeignKey(Lenguaje)
	torneo = models.ForeignKey(Torneo)
	archivo = models.FileField(upload_to=path)

class Caso_de_Prueba(models.Model):
	"""docstring for Caso_de_Prueba"""
	entrada = models.CharField(max_length=50)
	salida = models.CharField(max_length=50)	
	problema = models.ForeignKey(Problema)