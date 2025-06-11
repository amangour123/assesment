from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models import BaseModel

class Role(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(Role,on_delete=models.SET_NULL,null=True,blank=True,related_name = 'users')

