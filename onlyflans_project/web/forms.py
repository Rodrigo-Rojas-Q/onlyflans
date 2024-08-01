from django import forms
from .models import ContactForm

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['Correo_Electronico', 'Nombre', 'Mensaje']
        widgets = {
            'Correo_Electronico': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu correo electrónico'
            }),
            'Nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre'
            }),
            'Mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu mensaje aquí',
                'rows': 5
            }),
        }