from django.shortcuts import render
from apps.alunos.forms import LoginForms
from apps.alunos.forms import CadastroForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            
            nome=form["nome_login"].value()
            senha=form["password"].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
            )
        
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
            return redirect('login')
                  
    return render(request, 'templates/index.html', {'form': form})

def cadastro(request):
    form = CadastroForm()
    
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            
            nome=form["nome_cadastro"].value()
            email=form["email_cadastro"].value()
            senha=form["senha_cadastro"].value()
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuário já cadastrado!')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
                )
            
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
            
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')

