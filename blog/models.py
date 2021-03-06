from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

from .utils import from_cyrillic_to_eng


class CategoryBlog(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False,
                            verbose_name='Название категории')
    slug = models.CharField(max_length=100, blank=True, unique=True)
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Описание категории')
    comments = models.TextField(null=True, blank=True,
                                verbose_name='Комментарии')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категории блога'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(from_cyrillic_to_eng(self.name))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('categoryblog-detail', args=[str(self.slug)])


class TagBlog(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False,
                            verbose_name='Название тега')
    slug = models.CharField(max_length=100, blank=True, unique=True)
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Описание категории')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Тэг блога'
        verbose_name_plural = 'Тэги блога'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(from_cyrillic_to_eng(self.name))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tagblog-detail', args=[str(self.slug)])


class PostBlog(models.Model):
    title = models.CharField(max_length=160, null=False, blank=False,
                             verbose_name='Заголовок поста')
    slug = models.CharField(max_length=180, blank=True, unique=True)
    intro = RichTextField(null=False, blank=False,
                          verbose_name='Краткое описание поста')
    full_text = RichTextField(null=True, blank=True,
                              verbose_name='Полный текст поста')
    category = models.ForeignKey(CategoryBlog, on_delete=models.CASCADE,
                                 verbose_name='Категория')
    tags = models.ManyToManyField(TagBlog, verbose_name='Тэги')
    created_at = models.DateTimeField(auto_now_add=True)
    hits = models.IntegerField(verbose_name='Просмотры', default=0)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at', ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(from_cyrillic_to_eng(self.title))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('postblog-detail', args=[str(self.slug)])
