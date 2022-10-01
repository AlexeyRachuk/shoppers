from . import views
from django.urls import path

from .views import contact_page, contact_success

urlpatterns = [
    path('', contact_page),
    path('contact_success/', contact_success, name='contact_success')

]
