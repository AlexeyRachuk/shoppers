from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Форма регистрации /user/register/
from user_profile.models import Profile


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'required': True}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'required': True, 'type': 'password'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'required': True, 'type': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Форма авториизации /user/login/
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    password = forms.CharField(label='Пароль',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'required': True, 'type': 'password'}))


# Форма редактирования профиля /user/cabinet_editing/
class CabinetEditing(forms.ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    company = forms.CharField(label='Компания',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'required': False}))
    tel = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    zip_code = forms.CharField(label='Индекс',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    point = forms.CharField(label='Номер квартиры или офиса',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    descr = forms.CharField(label='Дополнительная информация',
                           widget=forms.Textarea(attrs={'class': 'form-control', 'required': False, 'rows': '5'}))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'company', 'tel', 'city', 'zip_code', 'address', 'point', 'descr']
