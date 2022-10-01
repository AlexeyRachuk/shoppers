from django.contrib.auth.models import User
from django.db import models


# Модель личного кабинета
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Логин', on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    company = models.CharField('Название оргинизации', max_length=100, help_text='Для юридических лиц', blank=True,
                               null=True)
    tel = models.CharField('Номер телефона', max_length=12)
    city = models.CharField('Город', max_length=100)
    zip_code = models.CharField('Индекс', max_length=10)
    address = models.CharField('Адрес доставки', max_length=100)
    point = models.CharField('Номер квартиры или офиса', max_length=100)
    descr = models.TextField('Дополнительная информация', blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


