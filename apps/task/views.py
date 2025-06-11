from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Task
from .serializers import TaskSerializer
from apps.user.permissions import IsAdminOrManager, IsAdmin, IsManager,IsAssigneeOrAdminManager

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdminOrManager()]
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        if user.role and user.role.name in ['admin', 'manager']:
            return Task.objects.all()
        return Task.objects.filter(assigned_to=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated, IsAssigneeOrAdminManager])
    def update_status(self, request, pk=None):
        task = self.get_object()
        user = request.user

        if task.assigned_to != user and not user.role or user.role.name not in ['admin', 'manager']:
            return Response({'detail': 'Not allowed'}, status=403)

        task.status = request.data.get('status', task.status)
        task.updated_by = user
        task.save()
        return Response(TaskSerializer(task).data)

