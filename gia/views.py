from django.views.generic import DetailView
from django.views.generic.base import RedirectView
from django.core import paginator
from .models import GiaTask, TaskType


class GiaTaskDetailView(DetailView):
    model = GiaTask


class TaskTypeDetailView(DetailView):
    model = TaskType
    task_paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TaskTypeDetailView, self).get_context_data(**kwargs)
        tasks = GiaTask.objects.filter(task_type=context['tasktype'].id).order_by('id')
        task_paginator = paginator.Paginator(tasks, self.task_paginate_by)
        page = self.request.GET.get('page')
        try:
            page_obj = task_paginator.page(page)
        except (paginator.PageNotAnInteger, paginator.EmptyPage):
            page_obj = task_paginator.page(1)
        context['page_obj'] = page_obj
        if task_paginator.count > self.task_paginate_by:
            context['is_paginated'] = True
        return context


class RedirectToEGEMath(RedirectView):
    url = '/gia/egem13/'


class RedirectToOGEMath(RedirectView):
    url = '/gia/ogem20/'
