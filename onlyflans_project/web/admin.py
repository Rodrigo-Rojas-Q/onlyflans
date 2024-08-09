from django.contrib import admin
from .models import Flan, ContactForm, Profile, Comment

# Register your models here.

admin.site.register(Flan)
admin.site.register(ContactForm)
admin.site.register(Profile)
admin.site.register(Comment)