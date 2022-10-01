from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from .models import Profile
from .forms import RegisterUserForm, LoginUserForm, CabinetEditing


# Регистрация новых пользователей /user/register/
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'profile/register.html'
    success_url = reverse_lazy('register_success')


# Представление успешной регистрации
def register_success(request):
    return render(request, 'profile/register_success.html')


# Авторизация /user/login/
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'profile/login.html'


# Выход
def logout_user(request):
    logout(request)
    return redirect('login')


# Личный кабинет /user/cabinet/
class UserCabinet(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'catalog_items'
    template_name = 'profile/cabinet.html'
    slug_field = "pk"

    def get_queryset(self):
        return Profile.objects.all().filter(user=self.request.user)


# Редактирование профиля /user/cabinet_editing/
class UserCabinetEditing(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = CabinetEditing
    template_name = 'profile/cabinet_edit.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))
