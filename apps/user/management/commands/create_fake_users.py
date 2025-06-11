from django.core.management.base import BaseCommand
from faker import Faker
from apps.user.models import User, Role
import random

class Command(BaseCommand):
    help = 'Create fake users'

    def handle(self, *args, **kwargs):
        fake = Faker()

        roles = list(Role.objects.all())
        if not roles:
            self.stdout.write("Please create roles first (Admin, Manager, User)")
            return

        for _ in range(20):
            role = random.choice(roles)
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123',
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                role=role
            )
            self.stdout.write(f'Created user: {user.username} - {role.name}')
