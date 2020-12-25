# Generated by Django 3.1.4 on 2020-12-17 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Название категории')),
                ('slug', models.CharField(blank=True, max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Категория блога',
                'verbose_name_plural': 'Категории блога',
            },
        ),
        migrations.CreateModel(
            name='TagBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Название тега')),
                ('slug', models.CharField(blank=True, max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Тэг блога',
                'verbose_name_plural': 'Тэги блога',
            },
        ),
        migrations.CreateModel(
            name='PostBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='Заголовок поста')),
                ('slug', models.CharField(blank=True, max_length=180, unique=True)),
                ('intro', models.TextField(verbose_name='Краткое описание поста')),
                ('full_text', models.TextField(blank=True, null=True, verbose_name='Полный текст поста')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoryblog', verbose_name='Категория')),
                ('tags', models.ManyToManyField(to='blog.TagBlog', verbose_name='Тэги')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]