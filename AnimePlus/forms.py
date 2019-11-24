from django import forms
from django.forms import ModelForm
from .models import Persona, Post

class FormPersona(ModelForm):
	class Meta:
		model = Persona
		fields = ['nombre', 'correo', 'fono', 'motivo', 'comentario']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)		