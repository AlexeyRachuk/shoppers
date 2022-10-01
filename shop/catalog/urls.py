from . import views
from django.urls import path

from .views import CatalogListView, CatalogDetailView, CatalogCategoryListView, FilterSize

urlpatterns = [
    path('', CatalogListView.as_view()),
    path('filter/', FilterSize.as_view(), name='size'),
    path('search/', views.Search.as_view(), name='search'),
    path('<slug:slug>/', CatalogDetailView.as_view(), name='catalog_detail'),
    path('category/<slug:cat_slug>/', CatalogCategoryListView.as_view(), name="catalog_category")

]


