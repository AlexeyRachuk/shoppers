from django.db import models


# Модель формы на странице контактов
class ContactFormPage(models.Model):
    name = models.CharField('Имя', max_length=20)
    tel = models.CharField('Телефон', max_length=50)
    email = models.CharField('Email', max_length=100)
    message = models.CharField('Сообщение', max_length=255)

    class Meta:
        verbose_name = "Заявки с формы на странице Контакты"
        verbose_name_plural = "Заявки с формы на странице Контакты"

    def __str__(self):
        return "Заявки с формы на странице Контакты"
