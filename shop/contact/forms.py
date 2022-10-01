from django import forms
from django.forms import TextInput, Textarea

from .models import *


# Форма на странице контактов
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormPage
        fields = ['name', 'tel', 'email', 'message']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя',
            }),
            "tel": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон',
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'rows': '7',
                'placeholder': 'Сообщение',
            })

        }
