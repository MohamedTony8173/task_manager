from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Task
from .mixins import SprintTaskMixin


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:task_list")


class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/task_form.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("tasks:task_detail", kwargs={"pk": self.object.id})


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "tasks/task_form.html"
    fields = "__all__"
    
    def get_success_url(self):
        return reverse_lazy("tasks:task_detail", kwargs={"pk": self.object.id})
