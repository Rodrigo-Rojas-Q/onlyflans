from django.db import models
from django.contrib.auth.models import User
import uuid

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    Correo_Electronico = models.EmailField()
    Nombre = models.CharField(max_length=64)
    Mensaje = models.TextField()

    def __str__(self):
        return self.Nombre

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    public_bio = models.BooleanField(default=True)
    public_birth_date = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username
    

    
    