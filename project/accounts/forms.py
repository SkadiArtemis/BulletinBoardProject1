from django import forms
from django.contrib.auth.models import User

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_name', 'email', 'first_name', 'last_name')


class Auth_codeForm(forms.Form):
    ode = forms.FileField(label='Код подтверждения регистрации')