# Generated by Django 3.1.3 on 2020-11-16 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='giatask',
            options={'verbose_name': 'Задача ГИА', 'verbose_name_plural': 'Задачи ГИА'},
        ),
        migrations.AddField(
            model_name='giatask',
            name='slug',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='giatask',
            name='title',
            field=models.CharField(default='', max_length=200, verbose_name='Название задания'),
            preserve_default=False,
        ),
    ]
