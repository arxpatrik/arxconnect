from django import forms

class LoginForms (forms.Form):
    nome_login=forms.CharField(
        label="Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'login-box',
                'placeholder' : 'Entre com o seu login'
            }
        )        

    )

    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'login-box',               
                'placeholder' : 'Entre com a sua senha'
            }            
        )
    )    

    lembrar_me = forms.BooleanField(
        label='Lembrar-me', 
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'forms-Chec'})
    )

class CadastroForms(forms.Form):

    nome_cadastro=forms.CharField(
        label='Nome de cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'login-box',
                'placeholder' : 'Ex: Patrik.Mateus'
            }
        )                
    )
    email=forms.EmailField(
        label = 'Email',
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs ={
                'class': 'login-box',
                'placeholder' : 'Ex: Wesley@gmail.com'
            }
        )
    )

    senha_1=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'login-box',               
                'placeholder' : 'Informe sua senha'
            }            
        )
    )
    senha_2=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'login-box',               
                'placeholder' : 'Informe sua senha Novamente'
            }            
        )
    )    