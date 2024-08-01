from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('welcome/', views.welcome, name='welcome'),
    path('base/', views.base, name='base'),
    path('contacto/', views.contacto, name='contacto'),
    path('exito/', views.exito, name='exito'),
]