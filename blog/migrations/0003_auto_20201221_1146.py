# Generated by Django 3.1.4 on 2020-12-21 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postblog_hits'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postblog',
            options={'ordering': ['-created_at'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]