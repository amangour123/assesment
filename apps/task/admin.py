from django.contrib import admin
from .models import *

# Register your models here

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','assigned_to','deadline','created_by']
admin.site.register(Task)
