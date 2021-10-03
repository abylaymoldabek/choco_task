from django.contrib.auth.models import User
from django.db import models

CHOICE_LIST = [(1, 'Admin'), (2, 'Employee'), (3, 'Guest')]


class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.SmallIntegerField(choices=CHOICE_LIST, default=3)

    def __str__(self):
        return f"{self.user} - {self.role}"


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    deadline = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    check_for_hour = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.deadline}"
