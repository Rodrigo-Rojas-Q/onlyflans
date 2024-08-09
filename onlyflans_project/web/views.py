from django.shortcuts import render, redirect, get_object_or_404
from . models import Flan, Profile, Comment
from . forms import ContactFormForm, LoginForm, ProfileForm, CommentForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html',{'flanes': flanes_publicos})

def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    # pasar el nombre de usuario al contexto
    context = {
        'flanes': flanes_privados,
        'username': request.user.get_username() #obtiene el nombre de usuario
    }
    return render(request,'welcome.html', context)

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

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('welcome') # redirige a la pagina de inicio
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = LoginForm()  
    
    return render(request, 'custom_login-html',{'form': form})


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    try:
        profile = Profile.objects.get(user=user)
        bio = profile.bio if profile.public_bio else "esta información es privada"
        birth_date = profile.birth_date if profile.public_birth_date else "esta información es privada"
    except Profile.DoesNotExist:
        bio = "esta información es privada"
        birth_date = "esta información es privada"
    
    data = {
        'user': user,
        'bio': bio,
        'birth_date': birth_date
    }
    return render(request, 'profile.html', data)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = Profile(user=request.user)
        
        bio = request.POST.get('bio', '')
        birth_date = request.POST.get('birth_date', None)
        
        print(f'Bio: {bio}, Birth Date: {birth_date}')  # Verifica que los datos se reciben correctamente
        
        profile.bio = bio
        profile.birth_date = birth_date
        profile.save()
        
        return redirect('profile', username=request.user.username)
    else:
        print(f'Current Bio: {profile.bio}, Current Birth Date: {profile.birth_date}')  # Verificar datos actuales
        context = {
            'user': request.user,
            'profile': profile,
            'bio': profile.bio,
            'birth_date': profile.birth_date  # Asegúrate de que birth_date está en el contexto
        }
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = Profile(user=request.user)  # Crear un perfil vacío si no existe
          
        return render(request, 'web/profile.html', context)
    
@login_required
def flan_detail(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    comments = flan.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.flan = flan
            comment.user = request.user
            comment.save()
            return redirect('flan_detail', slug=slug)
    else:
        comment_form = CommentForm()
    return render(request, 'flan_detail.html', {
        'flan': flan,
        'comments': comments,
        'comment_form': comment_form
    })