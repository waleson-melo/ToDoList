from django.urls import path

from task.views import ListTasks, DetailTask, CreateTask, UpdateTask, DeleteTask


urlpatterns = [
    path('', ListTasks.as_view(), name='task-list'),
    path('detalhe/<int:pk>/', DetailTask.as_view(), name='task-detail'),
    path('cadastrar/', CreateTask.as_view(), name='task-create'),
    path('atualizar/<int:pk>/', UpdateTask.as_view(), name='task-update'),
    path('deletar/<int:pk>/', DeleteTask.as_view(), name='task-delete'),
]
