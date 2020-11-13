from django.db import models
from .utils import from_cyrillic_to_eng


class Tag(models.Model):
    tag_name = models.CharField(max_length=40,
                                verbose_name='Тэг',
                                blank=False,
                                unique=True)
    slug = models.CharField(max_length=60, unique=True, blank=True)
    tag_description = models.TextField(
        verbose_name='Описание тэга', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.tag_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.tag_name))
        super().save(*args, **kwargs)


class Category(models.Model):
    category_name = models.CharField(max_length=80,
                                     verbose_name='Категория',
                                     blank=False,
                                     unique=True)
    slug = models.CharField(max_length=100, unique=True, blank=True)
    category_description = models.TextField(
        verbose_name='Описание категории', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.category_name)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=80,
                             verbose_name='Заголовок поста',
                             blank=False, null=False)
    slug = models.CharField(max_length=100, blank=True, unique=True)
    short_description = models.TextField(verbose_name='Краткое описание')
    full_text = models.TextField(verbose_name='Полный текст')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    category_post = models.ForeignKey(Category, on_delete=models.CASCADE,
                                      verbose_name='Категория')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.title))
        super().save(*args, **kwargs)
