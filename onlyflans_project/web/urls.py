from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [
    
    
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('welcome/', views.welcome, name='welcome'),
    path('base/', views.base, name='base'),
    path('contacto/', views.contacto, name='contacto'),
    path('exito/', views.exito, name='exito'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('flan/<slug:slug>/', views.flan_detail, name='flan_detail')
]