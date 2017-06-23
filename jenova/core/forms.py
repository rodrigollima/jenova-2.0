from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.PasswordInput(label='Senha')
