from django.shortcuts import render, redirect
from . models import Flan
from . forms import ContactFormForm
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html',{'flanes': flanes_publicos})

def about(request):
    return render(request, 'about.html')

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html',{'flanes': flanes_privados})

def base(request):
    return render(request, 'base.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exito/')
    else:
        form = ContactFormForm()
    return render(request, 'contacto.html', {'form':form})

def exito(request):
    return render(request, 'exito.html')
    
    