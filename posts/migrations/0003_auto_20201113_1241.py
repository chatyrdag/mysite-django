# Generated by Django 3.1.3 on 2020-11-13 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201113_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category_post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='posts.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='posts.Tag', verbose_name='Тэги'),
        ),
    ]
