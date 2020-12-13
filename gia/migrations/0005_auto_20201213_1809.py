# Generated by Django 3.1.4 on 2020-12-13 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gia', '0004_exam_tasktype'),
    ]

    operations = [
        migrations.AddField(
            model_name='giatask',
            name='solution',
            field=models.TextField(blank=True, null=True, verbose_name='Решение'),
        ),
        migrations.AddField(
            model_name='giatask',
            name='task_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gia.tasktype', verbose_name='Тип задания'),
            preserve_default=False,
        ),
    ]
