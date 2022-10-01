from django.contrib import admin
from django.db import models
from solo.admin import SingletonModelAdmin
from django.utils.safestring import mark_safe

from about.models import About, AboutTeam


# Раздел «О нас» в админке
@admin.register(About)
class AboutAdmin(SingletonModelAdmin):
    list_display = [field.name for field in About._meta.get_fields()]


# Раздел «Сотрудники» в админке
@admin.register(AboutTeam)
class AboutTeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'get_image', 'team_order', 'team_index', 'team_draft',)
    list_filter = ('team_name',)
    search_fields = ('team_name',)
    list_editable = ('team_order', 'team_index', 'team_draft')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.team_image.url} width="50" height="50"')

    get_image.short_description = 'Фото'
