from django.forms import ModelForm, widgets
from .models import Contacto

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nomContacto','apeContacto','rutContacto','telContacto','CorreoContacto','ComenContacto']
        widgets = {
            'nomContacto':widgets.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder': 'Ingrese su Nombre',
                    'id':'nombre'
                    }),
            'apeContacto': widgets.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder': 'Ingrese sus Apellidos',
                    'id':'apellidos'
                    }),
            'rutContacto':widgets.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder': 'Ingrese su Rut',
                    'id':'rut'
                    }),
            'telContacto':widgets.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder': '+ 56 9 0000 0000',
                    'id':'fono'
                    }),
            'CorreoContacto':widgets.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder': 'Ingrese su correo electrónico',
                    'id':'correo'
                    }),
            'ComenContacto':widgets.Textarea(
                attrs ={
                    'class':'form-control',
                    'placeholder': 'Ingrese su comentario',
                    'id':'comentario'
                    }),
        }