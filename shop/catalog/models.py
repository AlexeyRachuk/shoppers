from datetime import date

from django.db import models
from django.urls import reverse


# Модель категорий
class Category(models.Model):
    category_title = models.CharField('Название категории', max_length=100)
    category_url = models.SlugField('Ссылка категории', max_length=100, unique=True)

    def __str__(self):
        return self.category_title

    def get_absolute_url(self):
        return reverse('catalog_category', kwargs={'cat_slug': self.category_url})

    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товара"


# Модель размеров
class Size(models.Model):
    size_title = models.CharField('Размер', max_length=10)
    size_url = models.SlugField('Ссылка категории', max_length=100, unique=True)

    def __str__(self):
        return self.size_title

    def get_absolute_url(self):
        return reverse('size', kwargs={'size_slug': self.size_url})

    class Meta:
        verbose_name = "Размер товара"
        verbose_name_plural = "Размеры товара"


# Основная модель каталога
class Catalog(models.Model):
    catalog_title = models.CharField('Название товара', max_length=150)
    catalog_url = models.SlugField('Ссылка товара', help_text='Должна быть уникальна, формируется после сохранения',
                                   unique=True, max_length=200)
    catalog_descriptions = models.TextField('Описание товара')
    catalog_price = models.IntegerField('Цена товара')
    catalog_price_old = models.IntegerField('Зачеркнутая цена', blank=True, null=True)
    catalog_image = models.ImageField('Изображение товара', upload_to='images/catalog/')
    catalog_category = models.ForeignKey(Category, verbose_name='Категория товара', on_delete=models.SET_NULL,
                                         null=True)
    catalog_size = models.ManyToManyField(Size, verbose_name='Размеры', related_name='size_list')
    catalog_new_arrivals = models.BooleanField('Новое поступление?', default=False)
    catalog_date = models.DateField('Дата публикации', help_text='Обновив дату можно поднять товар в очередности',
                                    default=date.today)
    catalog_draft = models.BooleanField('Публикация товара', help_text='Отображение товара', default=True)

    def __str__(self):
        return self.catalog_title

    def get_absolute_url(self):
        return reverse("catalog_detail", kwargs={"slug": self.catalog_url})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
