from django.db import models
from .utils import from_cyrillic_to_eng


class GiaTask(models.Model):

    class ExamType(models.IntegerChoices):
        EGE = 1
        OGE = 2

    title = models.CharField(max_length=200, null=False,
                             verbose_name='Название задания')
    slug = models.CharField(max_length=250, blank=True, unique=True)
    task_text = models.TextField(null=False, verbose_name='Текст задания')
    exam = models.IntegerField(
        choices=ExamType.choices, default=ExamType.EGE, verbose_name='Тип экзамена')
    task_number = models.SmallIntegerField(
        verbose_name='Номер задания', null=False)
    file_with_solition = models.CharField(
        max_length=40, null=True, blank=True, verbose_name='Файл с решением')
    comments = models.TextField(
        null=True, blank=True, verbose_name='Комментарии')
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Задача ГИА'
        verbose_name_plural = 'Задачи ГИА'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.title))
        super().save(*args, **kwargs)
