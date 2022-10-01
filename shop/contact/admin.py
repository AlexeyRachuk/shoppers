from django.contrib import admin

from contact.models import ContactFormPage


# Представление в админке заявок с формы
@admin.register(ContactFormPage)
class FormContactPageAdmin(admin.ModelAdmin):
    list_display = ('name',)
