from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comentario
from django.forms import widgets

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class PostForm(forms.ModelForm):
    titulo = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'Título'}), required=True)
    slug = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'Slug'}), required=True)
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'Nueva publicación'}), required=True)
    categoria = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'Categoria'}), required=True)

    class Meta:
        model = Post 
        fields = ['titulo','slug','content', 'categoria']

class ComentarioForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'Ingrese su comentario', 'comentario': widgets.HiddenInput}), required=True )

    class Meta:
        model = Comentario
        fields = ['content']