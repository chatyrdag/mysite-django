# Generated by Django 3.1.3 on 2020-11-16 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gia', '0002_auto_20201116_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giatask',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарии'),
        ),
        migrations.AlterField(
            model_name='giatask',
            name='file_with_solition',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Файл с решением'),
        ),
    ]
