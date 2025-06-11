from django.db import models
from apps.core.models import BaseModel
from django.conf import settings
from django.utils import timezone

class Task(BaseModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('missed', 'Missed Deadline'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    deadline = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def is_overdue(self):
        return self.status != 'completed' and self.deadline < timezone.now()

