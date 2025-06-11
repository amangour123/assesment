from django.db import models
from django.utils import timezone
from django.conf import settings
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                            primary_key=True,
                            unique=True,
                            editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="%(class)s_created_by",on_delete=models.SET_NULL,null=True,blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="%(class)s_updated_by",on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        abstract = True

