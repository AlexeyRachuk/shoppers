# Generated by Django 4.1.1 on 2022-09-15 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_size_options_size_size_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'Размер товара', 'verbose_name_plural': 'Размеры товара'},
        ),
        migrations.AlterField(
            model_name='catalog',
            name='catalog_price_old',
            field=models.IntegerField(blank=True, null=True, verbose_name='Зачеркнутая цена'),
        ),
    ]
