
from django.urls import path
from . import views

urlpatterns = [
	path('Login/', views.Login, name='Login'),	
	path('Prueba/', views.Prueba, name='Prueba'),
	path('Noticias/', views.Noticias, name='Noticias'),
	path('Galeria/', views.Galeria, name='Galeria'),
	path('Contacto/', views.Creacion, name='Creacion'),	
	path('Enviado/', views.Creacion, name='Enviado'),
	path('Listado/', views.Listado, name='Listado'),
	path('Modificar/', views.Modificar, name='Modificar'),
	path('Eliminar/', views.Eliminar, name='Eliminar'),
	path('Filtrar/',views.Filtrar, name='Filtrar'),
	path('Recuperar/',views.Recuperar, name='Recuperar'),
	path('', views.post_list, name='post_list'),
]