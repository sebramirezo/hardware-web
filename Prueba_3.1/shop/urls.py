from os import name
from django.urls import path
from django.utils import html
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('index', views.index, name="index"),
    path('', views.index, name="index"),
    path('productos', views.productos, name="productos"),
    path('contacto', views.contactos, name="contactos"),
    path('contacto_form', views.contacto_form, name="contactos"),
    path('login', LoginView.as_view(template_name ='shop/login.html'), name="login"),
    path('admin_list', views.admin_list, name="admin_list"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('delete_comentario/<id>', views.delete_comentario, name="delete_comentario")
]