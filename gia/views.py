from django.shortcuts import render
from .models import GiaTask


def gia(request, exam, task=13, offset=1):

    if offset < 1:
        offset = 1

    if exam == 'oge' and task == 13:
        task = 19

    if exam == 'ege':
        exam_num = 1
        task_range = range(13, 20)
    else:
        exam_num = 2
        task_range = range(19, 26)

    total_tasks = GiaTask.objects.filter(
        exam=exam_num, task_number=task).count()
    pages_count = total_tasks // 10 + 1
    task_query = GiaTask.objects.filter(exam=exam_num, task_number=task).order_by('id')[
        (offset - 1) * 10:offset * 10 - 1]
    return render(request, 'gia.html', {
        'tasks': task_query,
        'task_number': task,
        'exam': exam,
        'task_range': task_range,
        'total_tasks': total_tasks,
        'pages_count': pages_count,
        'offset': offset,
        'offsetm1': offset - 1,
        'offsetp1': offset + 1,
        'pages_range': range(1, pages_count + 1)
    })


def show(request, task):

    task_query = GiaTask.objects.filter(slug=task)[0]
    exam_num = task_query.exam

    if exam_num == 1:
        exam = 'ege'
        task_range = range(13, 20)
    elif exam_num == 2:
        exam = 'oge'
        task_range = range(19, 26)

    return render(request, 'showsolution.html', {
        'task': task_query,
        'exam': exam,
        'task_range': task_range
    })
