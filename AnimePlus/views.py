from django.shortcuts import render
from .models import Persona, Post
from .forms import FormPersona, PostForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.

def Login(request) :
	return render(request, 'AnimePlus/Login.html')

def Prueba(request) : 
    return render(request, 'AnimePlus/Prueba.html')

def Noticias(request) :
    return render(request, 'AnimePlus/Noticias.html')

def Galeria(request) :
    return render(request, 'AnimePlus/Galeria.html')

def Listado(request) :
	# recuperamos a todas las personas de la BD
	listaPersonas = Persona.objects.all()
	return render(request, 'AnimePlus/Listado.html',
		{ 'listaPersonas' : listaPersonas,
		'cuantos' : len(listaPersonas)
		})

def Creacion(request) :        
	if request.method == 'POST' :
		form = FormPersona(request.POST)
		if form.is_valid() :
			persona = form.save()
			return render(request, 
				'AnimePlus/Enviado.html',
				{'persona' : persona})
	else :
		form = FormPersona()
		return render(request, 'AnimePlus/Contacto.html',
			{'form_fields' : form})

def Modificar(request, nombre):
	listaPersonas = Persona.objects.get(nombre=nombre)
	if request.method == 'GET' :
		form = FormPersona(instance = listaPersonas)
	else :
		form = FormPersona(request.POST, instance = listaPersonas)
		if form.is_valid():
			form.save()
			return redirect('AnimePlus:Contacto')
		return render(request, 'AnimePlus/Modificar.html',
			{'form_fields' : form})

def Eliminar(request, nombre):
	listaPersonas = Persona.objects.get(nombre=nombre)
	if request.method == 'POST' :
		form.delete() 
		return redirect('AnimePlus:Contacto')
	return render(request,
			'AnimePlus/Eliminar.html',
			{'persona' : persona})		

def Filtrar(request):
	if request.POST.get('nombre'):
		listaPersonas = Persona.filter(nombre=nombre)	
	return render(request, 
	"AnimePlus/Filtrar.html", 
	{'persona': persona, 'nombre':nombre})

def post_list(request):
	user = request.user
	if user.has_perm('AnimePlus.admin'):
		posts = Post.objects.filter(
			published_date__lte=timezone.now()).order_by('published_date')
		return render(request, 'AnimePlus/post_list.html', {'posts': posts})
	else:
		return render(request, 'AnimePlus/home.html')	
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def Recuperar(request):
	return render(request, 'AnimePlus/Recuperar.html')

