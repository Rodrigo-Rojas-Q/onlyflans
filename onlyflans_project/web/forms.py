from django import forms
from .models import ContactForm, Profile            

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
         
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'birth_date', 'public_bio', 'public_birth_date']
        
