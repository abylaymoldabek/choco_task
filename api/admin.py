from django.contrib import admin

from .models import Task, Role

admin.site.register(Task)
admin.site.register(Role)
