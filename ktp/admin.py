from django.contrib import admin
from .models import AcademicYear, Teacher, SchoolForm, Discipline, KTP


class KTPAdmin(admin.ModelAdmin):
	list_display = ('number_of_lesson', 'plan_date', 'theme',)
	list_filter = ('school_form', 'discipline_name',)


admin.site.register(AcademicYear)
admin.site.register(Teacher)
admin.site.register(SchoolForm)
admin.site.register(Discipline)
admin.site.register(KTP, KTPAdmin)
