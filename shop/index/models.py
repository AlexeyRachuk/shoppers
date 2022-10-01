from django.db import models
from django.views.generic import CreateView
from solo.models import SingletonModel


# Модель баннера на главной и приемуществ
class Index(SingletonModel):
    singleton_instance_id = 1
    banner_title = models.CharField('Заголовок баннера', max_length=50)
    banner_description = models.CharField('Описание баннера', max_length=150)
    banner_button = models.CharField('Кнопка баннера', max_length=50)
    banner_url = models.CharField('Ссылка кнопки', max_length=50)
    banner_image = models.ImageField('Изображение на баннере', upload_to='images/')

    def __str__(self):
        return "Главная и приемущества"

    class Meta:
        verbose_name = "Главная и приемущества"


# Модель иконок приемуществ
class IconBenefit(models.Model):
    title = models.CharField('Название иконки', max_length=50)
    icon_class = models.CharField('Класс иконки', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Иконки"
        verbose_name_plural = "Иконки"


# Модель приемуществ
class Benefit(models.Model):
    title = models.CharField('Название приемущества', max_length=50)
    description = models.CharField('Описание преимущества', max_length=200)
    icon = models.ForeignKey(IconBenefit, on_delete=models.CASCADE, related_name='benefit_icon')
    benefits = models.ForeignKey(Index, on_delete=models.CASCADE, related_name='benefits_id', default='')

    def __str__(self):
        return "Приемущества"

    class Meta:
        verbose_name = "Приемущества"
        verbose_name_plural = "Приемущества"


# Модель акции на главной
class Action(SingletonModel):
    singleton_instance_id = 1
    action_block_title = models.CharField('Заголовок блока распродажи', max_length=50)
    action_title = models.CharField('Заголовок акции', max_length=100)
    action_date = models.CharField('Даты проведения', max_length=150)
    action_description = models.TextField('Описани акции')
    action_button = models.CharField('Название кнопки', max_length=50)
    action_url = models.CharField('Ссылка кнопки', max_length=50)
    action_image = models.ImageField('Изображение акции', upload_to='images/')
    action_active = models.BooleanField('Акция активна?', default=False)

    def __str__(self):
        return "Акция"

    class Meta:
        verbose_name = "Акция"


# Модель контактов
class Contact(SingletonModel):
    contact_adress = models.CharField('Адрес', max_length=200)
    contact_tel = models.CharField('Телефон', max_length=60)
    contact_email = models.CharField('Email', max_length=100)
    copywrite = models.CharField('Копирайт в подвале', max_length=100)

    def __str__(self):
        return "Контакты"

    class Meta:
        verbose_name = "Контакты"