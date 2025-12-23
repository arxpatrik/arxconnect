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

