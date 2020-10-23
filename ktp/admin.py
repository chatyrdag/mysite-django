from django.contrib import admin
from .models import AcademicYear, Teacher, SchoolForm, Discipline, KTP


admin.site.register(AcademicYear)
admin.site.register(Teacher)
admin.site.register(SchoolForm)
admin.site.register(Discipline)
admin.site.register(KTP)
