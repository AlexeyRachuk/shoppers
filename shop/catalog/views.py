from django.db.models import Min, Max
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Catalog, Size


# Представление размеров
class SizeList:
    def get_size(self):
        return Size.objects.all()


# Представление списка товаров
class CatalogListView(SizeList, ListView):
    model = Catalog
    queryset = Catalog.objects.filter(catalog_draft=True).order_by('-catalog_date')
    template_name = 'catalog/catalog.html'
    paginate_by = 9


# Представление детальной товара
class CatalogDetailView(DetailView):
    model = Catalog
    slug_field = 'catalog_url'
    template_name = 'catalog/catalog-single.html'
    context_object_name = 'catalog'


# Представление списка товаров по категориям
class CatalogCategoryListView(SizeList, ListView):
    model = Catalog
    template_name = 'catalog/catalog.html'
    paginate_by = 9

    def get_queryset(self):
        return Catalog.objects.filter(catalog_category__category_url=self.kwargs['cat_slug'],
                                      catalog_draft=True).order_by('-catalog_date')


# Фильтр по размерам
class FilterSize(SizeList, ListView):
    model = Catalog
    template_name = 'catalog/catalog.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = Catalog.objects.filter(catalog_size__in=self.request.GET.getlist('size'),
                                          catalog_draft=True).order_by('-catalog_date')
        return queryset


# Фильтр по цене
class FilterPrice(SizeList, ListView):
    model = Catalog
    template_name = 'catalog/catalog.html'
    paginate_by = 9

    def get_queryset(self):
        queryset_price = Catalog.objects.aggregate(Min('catalog_price'), Max('catalog_price'))

        return queryset_price


# Поиск
class Search(ListView):
    model = Catalog
    template_name = 'catalog/catalog.html'
    paginate_by = 9

    def get_queryset(self):
        q = self.request.GET.get('q').capitalize()
        return Catalog.objects.filter(catalog_title__icontains=q,
                                      catalog_draft=True).order_by('-catalog_date')


def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['q'] = f'search={self.request.GET.get("q")}&'
    return context
