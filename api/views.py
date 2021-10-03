from .permissions import GuestPermission, AdminPermission, EmployeePermission
from .serializers import TaskSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import permissions


from .models import Task


class TaskViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    permission_classes = [GuestPermission | AdminPermission | EmployeePermission]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
