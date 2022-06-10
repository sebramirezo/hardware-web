from shop.forms import ContactoForm
from django.shortcuts import redirect, render
from .models import Contacto
# Create your views here.

def index(request):
    return render(request, 'shop/index.html',)

def productos(request):
    return render(request, 'shop/productos.html',)

def contactos(request):
    return render(request, 'shop/contacto.html',)

def nosotros(request):
    return render(request, 'shop/nosotros.html',)

def contacto_form(request):
    contexto = {
        'form':ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje'] = "Hemos recibido su mensaje! Nos contactaremos a la brevedad posible."
    return render(request, 'shop/contacto_form.html', contexto)

def admin_list(request):
    listado_consultas = Contacto.objects.all()
    datos = {
        'listado_consultas':listado_consultas
    }
    return render(request, 'shop/admin_list.html', datos)

def delete_comentario(request, id):
    listado_consultas = Contacto.objects.get(rutContacto = id)
    listado_consultas.delete()
    return redirect(to="admin_list")