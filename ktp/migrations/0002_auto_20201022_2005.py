# Generated by Django 3.1.2 on 2020-10-22 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ktp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academicyear',
            options={'verbose_name': 'Учебный год', 'verbose_name_plural': 'Учебные года'},
        ),
        migrations.AlterModelOptions(
            name='discipline',
            options={'verbose_name': 'Дисциплина', 'verbose_name_plural': 'Дисциплины'},
        ),
        migrations.AlterModelOptions(
            name='ktp',
            options={'verbose_name': 'КТП', 'verbose_name_plural': 'КТП'},
        ),
        migrations.AlterModelOptions(
            name='schoolform',
            options={'verbose_name': 'Класс', 'verbose_name_plural': 'Классы'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Учитель', 'verbose_name_plural': 'Учителя'},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.CharField(blank=True, max_length=50, verbose_name='Электронная почта'),
        ),
    ]
