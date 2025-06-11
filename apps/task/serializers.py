from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'deadline', 'status',
            'assigned_to', 'assigned_to_username', 'created_at'
        ]
        read_only_fields = ['created_at']