from django.db import models
from solo.models import SingletonModel


# Модель страницы «О нас»
class About(SingletonModel):
    about_title = models.CharField('Заголовок страницы', max_length=60)
    about_description = models.TextField('Описание страницы')
    about_image = models.ImageField('Изображение страницы', upload_to='images/')

    def __str__(self):
        return "О нас"

    class Meta:
        verbose_name = "О нас"


# Модель сотрудников
class AboutTeam(models.Model):
    team_name = models.CharField('Имя сотрудника', max_length=100)
    team_post = models.CharField('Должность', max_length=100)
    team_image = models.ImageField('Фото сотрудника', upload_to='images/')
    team_order = models.SmallIntegerField('Порядок', default=0)
    team_index = models.BooleanField('Выводить сотрудника на главной?', default=False,
                                     help_text='Не больше 4 сотрудников для корректного отображения')
    team_draft = models.BooleanField('Публикация', default=False)

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = "Сотрудники"
        verbose_name_plural = "Сотрудники"
