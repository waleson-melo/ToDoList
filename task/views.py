from typing import Any
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from task.models import Task


class ListTasks(LoginRequiredMixin, ListView):
    template_name = 'task_list.html'
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('pesquisa') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['pesquisa'] = search_input

        return context


class DetailTask(LoginRequiredMixin, DetailView):
    template_name = 'task_detail.html'
    model = Task
    context_object_name = 'task'

    def get(self, request, *args, **kwargs):
        try:
            task = self.get_object()

            if task.user == request.user:
                return super().get(request, *args, **kwargs)
            else:
                messages.add_message(request, messages.WARNING, 'A tarefa que você está procurando não foi encontrada.')
                return redirect(reverse('task-list'))
        except:
            messages.error(request, 'A tarefa que você está procurando não foi encontrada.')
            return reverse_lazy('task_list')


class CreateTask(LoginRequiredMixin, CreateView):
    template_name = 'task_form.html'
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(CreateTask, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateTask, self).get_context_data(**kwargs)
        context['page_name'] = 'Cadastrar Tarefa'

        return context


class UpdateTask(LoginRequiredMixin, UpdateView):
    template_name = 'task_form.html'
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task-list')

    def get(self, request, *args, **kwargs):
        try:
            task = self.get_object()

            if task.user == request.user:
                return super().get(request, *args, **kwargs)
            else:
                messages.add_message(request, messages.WARNING, 'A tarefa que você está procurando não foi encontrada.')
                return redirect(reverse('task-list'))
        except:
            messages.error(request, 'A tarefa que você está procurando não foi encontrada.')
            return reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateTask, self).get_context_data(**kwargs)
        context['page_name'] = 'Atualizar Tarefa'

        return context


class DeleteTask(LoginRequiredMixin, DeleteView):
    template_name = 'task_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')

    def get(self, request, *args, **kwargs):
        try:
            task = self.get_object()

            if task.user == request.user:
                return super().get(request, *args, **kwargs)
            else:
                messages.add_message(request, messages.WARNING, 'Não foi possivel deletar a tarefa, pois não foi encontrada.')
                return redirect(reverse('task-list'))
        except:
            messages.error(request, 'A tarefa que você está procurando não foi encontrada.')
            return reverse_lazy('task_list')
