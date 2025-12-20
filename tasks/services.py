from django.shortcuts import get_object_or_404
from .models import Sprint


def can_add_task_to_sprint(task, sprint_id):
    sprint = get_object_or_404(Sprint, id=sprint_id)
    return sprint.start_date <= task.created_at.date <= sprint.end_date
