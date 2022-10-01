from django.contrib import admin
from solo.admin import SingletonModelAdmin

from index.models import IconBenefit, Benefit, Index, Action, Contact


# Иконки в админке
@admin.register(IconBenefit)
class IconBenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class')


# Приемущества в админке
class BenefitAdmin(admin.TabularInline):
    model = Benefit
    fields = ('title', 'description', 'icon')
    extra = 1


# Представление данных на главной и приемуществ в админке
@admin.register(Index)
class IndexAdmin(SingletonModelAdmin):
    inlines = [BenefitAdmin]


# Представление акции в админке
@admin.register(Action)
class ActionAdmin(SingletonModelAdmin):
    list_display = [field.name for field in Action._meta.get_fields()]


# Представление контактов в админке
@admin.register(Contact)
class ContactAdmin(SingletonModelAdmin):
    list_display = [field.name for field in Contact._meta.get_fields()]
