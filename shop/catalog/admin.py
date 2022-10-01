from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Catalog, Category, Size


# Представление каталога в админке
@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        'catalog_title', 'get_image', 'catalog_category', 'catalog_price', 'catalog_date', 'catalog_new_arrivals',
        'catalog_draft',)
    list_filter = ('catalog_category',)
    search_fields = ('catalog_title',)
    list_editable = ('catalog_date', 'catalog_new_arrivals', 'catalog_draft',)
    filter_horizontal = ('catalog_size',)
    prepopulated_fields = {'catalog_url': ('catalog_title',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.catalog_image.url} width="100" height="60"')

    get_image.short_description = 'Фото товара'


# Категории в админке
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title',)
    prepopulated_fields = {'category_url': ('category_title',)}


# Размеры в админке
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size_title',)
    prepopulated_fields = {'size_url': ('size_title',)}
