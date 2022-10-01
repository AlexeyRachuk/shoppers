# Generated by Django 4.1.1 on 2022-09-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_profile_descr_profile_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='descr',
            field=models.TextField(blank=True, verbose_name='Дополнительная информация'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='point',
            field=models.CharField(max_length=100, verbose_name='Номер квартиры или офиса'),
        ),
    ]
