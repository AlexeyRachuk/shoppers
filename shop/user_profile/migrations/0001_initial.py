# Generated by Django 4.1.1 on 2022-09-18 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('company', models.CharField(blank=True, help_text='Для юридических лиц', max_length=100, null=True, verbose_name='Название оргинизации')),
                ('tel', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('city', models.CharField(default='Россия', max_length=100, verbose_name='Город')),
                ('zip_code', models.IntegerField(max_length=10, verbose_name='Индекс')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес доставки')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Логин')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
            },
        ),
    ]
