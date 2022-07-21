from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.core.validators import EmailValidator, RegexValidator

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,validators=[EmailValidator])
    password1 = forms.CharField(widget=forms.PasswordInput,
    validators=[RegexValidator("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", message="Password must contain atleast 8 characters with one special character")])
    class Meta:
        model = User
        fields = ("username", "email", "password1","password2")

    

            