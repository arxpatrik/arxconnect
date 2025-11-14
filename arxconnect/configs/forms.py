from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import NivelAcesso, Permissao

class UsuarioCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telefone = forms.CharField(required=False, max_length=20)
    nivel = forms.ModelChoiceField(queryset=NivelAcesso.objects.none())
    permissoes = forms.ModelMultipleChoiceField(queryset=Permissao.objects.none(), widget=forms.CheckboxSelectMultiple, required=False)
    
    class Meta (UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nivel"].queryset = NivelAcesso.objects.all()
        self.fields["permissoes"].queryset = Permissao.objects.all()