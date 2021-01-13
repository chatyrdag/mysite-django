from django.shortcuts import render
from .models import Train, UserPerformTrain
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.timezone import get_current_timezone
import json
import datetime


@login_required
def train(request, train_type):
    train_obj = Train.objects.get(train_type=train_type)
    return render(request, 'train.html', {'train': train_obj})


@ensure_csrf_cookie
@login_required
def performed_train_rec(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        user_id = post_data.get('user_id')
        train_id = post_data.get('train_id')
        date_time = datetime.datetime.fromtimestamp(post_data.get('date_time'), tz=get_current_timezone())
        total_tasks = str(post_data.get('total_tasks'))
        correct_perf_tasks = str(post_data.get('correct_perf_tasks'))
        level_achieved = str(post_data.get('level_achieved'))
        data = str(post_data.get('data'))

        upt = UserPerformTrain(date_time=date_time, total_tasks=total_tasks,
                               correct_perf_tasks=correct_perf_tasks,
                               level_achieved=level_achieved,
                               data=data)
        u = User.objects.get(id=user_id)
        t = Train.objects.get(id=train_id)
        upt.user = u
        upt.train = t
        upt.save()

        print(user_id, train_id, date_time, total_tasks, correct_perf_tasks, level_achieved,  data)
    return JsonResponse({"status": "OK"})
