# Generated by Django 4.1.1 on 2022-09-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_action_action_url_alter_index_banner_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_adress', models.CharField(max_length=200, verbose_name='Адрес')),
                ('contact_tel', models.CharField(max_length=60, verbose_name='Телефон')),
                ('contact_email', models.CharField(max_length=100, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Контакты',
            },
        ),
        migrations.AlterModelOptions(
            name='benefit',
            options={'verbose_name': 'Приемущества', 'verbose_name_plural': 'Приемущества'},
        ),
        migrations.RemoveField(
            model_name='index',
            name='contact_adress',
        ),
        migrations.RemoveField(
            model_name='index',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='index',
            name='contact_tel',
        ),
    ]
