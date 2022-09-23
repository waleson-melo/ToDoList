from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from task.models import Task


class ListTasks(ListView):
    template_name = 'task_list.html'
    model = Task
    context_object_name = 'tasks'


class DetailTask(DetailView):
    template_name = 'task_detail.html'
    model = Task
    context_object_name = 'task'


class CreateTask(CreateView):
    template_name = 'task_form.html'
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super(CreateTask, self).get_context_data(**kwargs)
        context['page_name'] = 'Cadastrar Tarefa'

        return context


class UpdateTask(UpdateView):
    template_name = 'task_form.html'
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateTask, self).get_context_data(**kwargs)
        context['page_name'] = 'Atualizar Tarefa'

        return context


class DeleteTask(DeleteView):
    template_name = 'task_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
