from django.core import validators
from django import forms
from .models import Book


class BookRegistration(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name','isbn']
        