from django.shortcuts import render
from django.http import HttpResponse
from .models import KTP, SchoolForm, Discipline


def index(request):
    return render(request, 'ktp_index.html')


def ktp(request, form, discipline):
    query_school_form = SchoolForm.objects.filter(form_name=form)
    form_id = query_school_form[0].id
    query_discipline = Discipline.objects.filter(id=discipline)
    discipline_name = query_discipline[0].discipline_name
    qs = KTP.objects.filter(school_form=form_id, discipline_name=discipline).order_by('number_of_lesson')
    return render(request, 'ktp.html', {
        'lessons_list': qs,
        'discipline_name': discipline_name,
        'form': form,
    })
