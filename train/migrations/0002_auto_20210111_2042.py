# Generated by Django 3.1.5 on 2021-01-11 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userperformtrain',
            old_name='train_type',
            new_name='train_id',
        ),
    ]