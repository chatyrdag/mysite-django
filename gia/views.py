from django.views.generic import ListView, DetailView
from .models import GiaTask


class ShowSolution(DetailView):
    model = GiaTask
    template_name = 'gia/showsolution.html'
    context_object_name = 'task'
    exam_dict = {1: 'ege', 2: 'oge'}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.task_range = range(13, 20)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam'] = self.exam_dict[context['task'].exam]
        if context['exam'] == 'oge':
            self.task_range = range(19, 26)
        context['task_range'] = self.task_range
        return context


class GIAList(ListView):
    template_name = 'gia/gia.html'
    context_object_name = 'gia_list'
    exam_dict = {'ege': 1, 'oge': 2}
    paginate_by = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.task_number = 13
        self.task_range = range(13, 20)

    def get_queryset(self):
        if self.kwargs.get('task'):
            self.task_number = self.kwargs['task']
        elif self.kwargs['exam'] == 'oge':
            self.task_number = 19
        return GiaTask.objects.filter(exam=self.exam_dict[self.kwargs['exam']],
                                      task_number=self.task_number).order_by('id')

    def get_context_data(self, **kwargs):
        context = super(GIAList, self).get_context_data(**kwargs)
        context['exam'] = self.kwargs['exam']
        if self.kwargs['exam'] == 'oge':
            self.task_range = range(19, 26)
        context['task_range'] = self.task_range
        context['task_number'] = self.task_number
        return context
