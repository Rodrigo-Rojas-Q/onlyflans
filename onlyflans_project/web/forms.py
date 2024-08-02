from django import forms
from .models import ContactForm

class ContactFormForm(forms.ModelForm):
    Correo_Electronico = forms.EmailField(label='Correo')
    Nombre = forms.CharField(max_length=64, label='Nombre')
    Mensaje = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40, 'class': 'form-control'})
    )
    class Meta:
         model = ContactForm
         fields = ['Correo_Electronico', 'Nombre', 'Mensaje']