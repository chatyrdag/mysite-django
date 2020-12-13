from django.contrib import admin
from .models import GiaTask, Exam, TaskType


admin.site.register(GiaTask)
admin.site.register(Exam)
admin.site.register(TaskType)
