from django import forms
from django.contrib import messages

class LoginForms(forms.Form):
    
    nome_login = forms.CharField(
        label='Usuário', 
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nome de Usuário",
            }
        )
    )
    
    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua Senha",
            }
            ),
    )
    
class CadastroForm(forms.Form):
    
    nome_cadastro = forms.CharField(
        label='Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite seu Nome Completo",
            }            
        )
    )
    
    email_cadastro = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
            "class":"form-control",
            "placeholder":"Digite seu E-mail",
            }
        )   
    )
    
    senha_cadastro = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua Senha",
            }
            ),
    )
    
    senha_confirmacao = forms.CharField(
        label='Digite sua senha novamente',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirme sua Senha",
            }
            ),
    )
    
# O método abaixo é para validar se o nome    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome.strip()
            if " " in nome:
                raise forms.ValidationError("O nome não pode conter espaços")
            else:
                return nome

# Esse método é para  validar se as 2 senhas são iguais
    def clean_senha_confirmacao(self):
        senha_cadastro = self.cleaned_data.get("senha_cadastro")
        senha_confirmacao = self.cleaned_data.get("senha_confirmacao")
        if senha_cadastro and senha_confirmacao:
            if senha_cadastro != senha_confirmacao:
                raise forms.ValidationError("As senhas não conferem")
            else:
                return senha_confirmacao
    