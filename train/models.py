from django.db import models
from django.contrib.auth.models import User


class Train(models.Model):
    train_type = models.CharField(max_length=40,
                                  verbose_name='Тип тренажёра',
                                  blank=False, unique=True)
    name = models.CharField(max_length=100,
                            verbose_name='Название тренажёра',
                            blank=False)
    short_instruction = models.CharField(max_length=100,
                                         verbose_name='Краткая инструкция',
                                         blank=True, null=True)
    description = models.TextField(verbose_name='Описание тренажёра',
                                   blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Тренажёр"
        verbose_name_plural = "Тренажёры"

    def __str__(self):
        return self.name


class UserPerformTrain(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    train_type = models.ForeignKey(Train, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    total_tasks = models.SmallIntegerField()
    level_achieved = models.SmallIntegerField(default=1)
    correct_perf_tasks = models.SmallIntegerField()
    data = models.JSONField()
