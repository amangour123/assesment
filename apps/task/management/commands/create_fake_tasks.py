from django.core.management.base import BaseCommand
from faker import Faker
from apps.task.models import Task
from apps.user.models import User
import random
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Create fake tasks'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = User.objects.all()

        if not users:
            self.stdout.write("No users found. Create fake users first.")
            return

        for _ in range(50):
            user = random.choice(users)
            deadline = timezone.now() + timedelta(days=random.randint(-5, 10))
            status = random.choice(['pending', 'in_progress', 'completed', 'missed'])

            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.text(),
                assigned_to=user,
                deadline=deadline,
                status=status,
                created_by=user,
                updated_by=user
            )
            self.stdout.write(f'Created task: {task.title} for user {user.username}')
