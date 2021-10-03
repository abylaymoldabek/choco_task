from datetime import timedelta

from celery import shared_task
from django.core.mail import EmailMessage

from api.models import Task
from todo_drf import settings


@shared_task
def check_for_deadlines():
    tasks = Task.objects.filter(completed=False)
    for task in tasks:
        if not task.check_for_hour and task.deadline >= (task.deadline - timedelta(hours=1)):
            email = EmailMessage(subject='You have a task',
                                 body='You have one hour for completed task',
                                 from_email=settings.EMAIL_HOST_USER,
                                 to=[task.user.email])
            email.send(fail_silently=False)
            task.check_for_hour = True
            task.save()
