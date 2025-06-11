from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from apps.task.models import Task
from apps.user.models import User

class Command(BaseCommand):
    help = 'Mark overdue tasks as missed and deactivate users with 5+ missed tasks in the last 7 days'

    def handle(self, *args, **kwargs):
        now = timezone.now()

        # 1. Mark overdue tasks as missed
        overdue_tasks = Task.objects.filter(
            status__in=['pending', 'in_progress'],
            deadline__lt=now
        )
        updated_count = 0
        for task in overdue_tasks:
            task.status = 'missed'
            task.save()
            updated_count += 1

        self.stdout.write(self.style.SUCCESS(f"Marked {updated_count} tasks as missed."))

        # 2. Deactivate users with 5+ missed tasks in the last 7 days
        one_week_ago = now - timedelta(days=7)
        affected_users = 0
        for user in User.objects.filter(is_active=True):
            missed_count = user.tasks.filter(status='missed', deadline__gte=one_week_ago).count()
            if missed_count >= 5:
                user.is_active = False
                user.save()
                affected_users += 1
                self.stdout.write(f"Deactivated user: {user.username} (missed: {missed_count})")

        self.stdout.write(self.style.SUCCESS(f"Deactivated {affected_users} users with 5+ missed tasks."))
