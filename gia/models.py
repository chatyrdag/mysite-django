from django.db import models
from .utils import from_cyrillic_to_eng


class Exam(models.Model):
    name = models.CharField(max_length=80, null=False,
                            verbose_name='Экзамен')
    slug = models.CharField(max_length=100, blank=True, unique=True)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    comments = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class TaskType(models.Model):
    task_number = models.SmallIntegerField(verbose_name='Номер задания', null=False)
    slug = models.CharField(max_length=40, null=False, blank=True, unique=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,
                             verbose_name='Тип экзамена')
    description = models.TextField(verbose_name='Описание задания', null=True, blank=True)
    comments = models.TextField(verbose_name='Комментарии', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Тип задания'
        verbose_name_plural = 'Типы задания'

    def __str__(self):
        return str(self.exam) + ' ' + str(self.task_number)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.exam) + str(self.task_number))
        super().save(*args, **kwargs)


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
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE,
                                  verbose_name='Тип задания')
    task_number = models.SmallIntegerField(
        verbose_name='Номер задания', null=False)
    solution = models.TextField(null=True, blank=True, verbose_name='Решение')
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
